## GitHub Stars Scrapper

**GitHub Stars Scrapper** is a powerful Python tool designed to help gather email addresses and usernames of individuals who have starred a GitHub repository. This tool leverages multithreading to efficiently scrape GitHub and retrieve data without requiring an API key. It’s an excellent resource for developers who want to connect with those interested in their projects.

### Key Features

- **Multithreaded Scraping**: Quickly retrieve stargazers' emails and usernames using multiple threads for faster processing.
- **No API Key Required**: Access GitHub stargazer data directly without needing an API key.
- **Simple and Easy to Use**: Set up and run the scrapper with minimal configuration.
- **Customizable Output**: Save results as a list of emails, usernames, or both in text files.

### Installation

Install GitHub Stars Scrapper via `pip`:

```shell
pip install github-stars-scrapper
```

### Usage

Using GitHub Stars Scrapper is straightforward. Here’s how to get started:
```shell
import github_stars_scrapper

# Initialize the Scrapper
scrapper = github_stars_scrapper.Crawler(threads=16, target="[YourGitHubUsername]/repository-name")

# Run the Scrapper
scrapper.run()

# Print the results
scrapper.print_results()

# Save results to a file
scrapper.save_results("emails", "emails.txt")
scrapper.save_results("stargazers", "stargazers.txt")
scrapper.save_results("all", "all.txt")
```