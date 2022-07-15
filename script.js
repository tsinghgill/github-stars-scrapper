function fetchCustomerMedia() {
  const requestOptions = {
    method: 'GET',
    redirect: 'follow',
  };

  return fetch(
    `https://photorankapi-a.akamaihd.net/customers/215757/media/shuffled?version=v2.2&auth_token=0a40a13fd9d531110b4d6515ef0d6c529acdb59e81194132356a1b8903790c18&rights_given=1&disable_embedded_streams=1&disable_embedded_categories=1`,
    requestOptions
  ).then(resp => {
    return resp.json();
  });
}

function renderImage(json) {
  const modalHeader = document.querySelector('.modal-header');
  const modalBody = document.querySelector('.modal-body');
  
  modalHeader.innerHTML = '';
  modalBody.innerHTML = '';

  let img = undefined;
  let imgText = 'N/A';

  if (
    json.metadata?.message &&
    json.metadata?.message === 'OK' &&
    json.data?._embedded?.media.length > 0
  ) {
    const media = json.data._embedded.media;

    const randomMedia = media[Math.floor(Math.random() * media.length)];

    img = randomMedia.images.mobile;
    imgText =
      randomMedia?.caption?.length > 0
        ? randomMedia.caption
        : 'No Caption Available';

    const p = document.createElement('p');
    p.innerHTML = `<div>${imgText}</div>`;
    modalHeader.appendChild(p);

    const div = document.createElement('div');
    div.innerHTML = '<img src="' + img + '">';
    modalBody.appendChild(div);
  }
}

let media;
document.addEventListener('DOMContentLoaded', async function () {
  media = await fetchCustomerMedia();
});

var modal = document.getElementById('myModal');

var btn = document.getElementById('myBtn');

btn.onclick = function () {
  modal.style.display = 'block';
  renderImage(media);
};

var span = document.getElementsByClassName('close')[0];

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = 'none';
  }
};
