import requests
import re
import threading
import time
from bs4 import BeautifulSoup
from tqdm import tqdm

class Crawler:
    def __init__(self, threads: int, target: str) -> None:
        self.threads = threads
        self.username, self.repository = target.split('/')
        self.stargazers = []
        self.emails = {}
    
    def fetch_stargazers(self, page=1):
        url = f'https://github.com/{self.username}/{self.repository}/stargazers?page={page}'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            stargazers = soup.find_all('img', {'class': 'avatar avatar-user'})

            for stargazer in stargazers:
                username = stargazer['alt'][1:]  # Extract username
                self.stargazers.append(username)
                self.emails[username] = "Not retrieved"

            if stargazers:  # If stars were found, fetch the next page
                self.fetch_stargazers(page + 1)
        elif response.status_code == 429:  # Handle rate limiting
            time.sleep(1)
            self.fetch_stargazers(page)
    
    def fetch_email(self, username):
        url = f'https://github.com/{username}'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            latest_commit = soup.find('a', href=re.compile(f'/{username}/.*/commit/'))

            if latest_commit:
                commit_url = f'https://github.com{latest_commit["href"]}.patch'
                patch_response = requests.get(commit_url)
                email_match = re.search(r'<(.*?)>', patch_response.text)
                
                if email_match and "noreply" not in email_match.group(1):
                    return email_match.group(1)
        return None

    def run(self):
        start_time = time.time()
        print(f"[+] Target: {self.username}/{self.repository}")
        print(f"[+] Starting crawler with {self.threads} threads")
        
        self.fetch_stargazers()
        print(f"[+] Found {len(self.stargazers)} stargazers")
        
        self.pbar = tqdm(total=len(self.stargazers), desc="Fetching emails", unit="user")
        thread_list = []

        # Split stars into chunks based on the number of threads
        chunk_size = len(self.stargazers) // self.threads
        stargazer_chunks = [self.stargazers[i:i + chunk_size] for i in range(0, len(self.stargazers), chunk_size)]

        # Start threads for each chunk
        for chunk in stargazer_chunks:
            thread = threading.Thread(target=self.fetch_emails_from_chunk, args=(chunk,))
            thread_list.append(thread)
            thread.start()

        for thread in thread_list:
            thread.join()

        self.pbar.close()
        print(f"[+] Crawler finished in {time.time() - start_time:.2f} seconds")
    
    def fetch_emails_from_chunk(self, chunk):
        for stargazer in chunk:
            email = self.fetch_email(stargazer)
            if email:
                self.emails[stargazer] = email
            self.pbar.update(1)

    def save_results(self, mode: str, file: str):
        with open(file, 'w') as f:
            if mode == "emails":
                for email in set(self.emails.values()):
                    if email != "Not retrieved":
                        f.write(email + '\n')
            elif mode == "stargazers":
                for stargazer in self.stargazers:
                    f.write(stargazer + '\n')
            elif mode == "all":
                for username, email in self.emails.items():
                    f.write(f"{username}: {email}\n")
            else:
                print("[!] Unsupported mode. Use 'emails', 'stargazers', or 'all'.")
        print(f"[+] Results saved to {file}")

if __name__ == "__main__":
    crawler = Crawler(threads=16, target="Frikallo/MISST")
    crawler.run()
    crawler.save_results("emails", "emails.txt")
    crawler.save_results("stargazers", "stargazers.txt")
    crawler.save_results("all", "all.txt")