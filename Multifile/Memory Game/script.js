document.addEventListener("DOMContentLoaded", () => {
  const gridContainer = document.querySelector(".grid-container");
  let cards = [];
  let firstCard = null, secondCard = null;
  let lockBoard = false;
  let score = 0;

  document.querySelector(".score").textContent = score;

  fetch("./data/cards.json")
    .then(res => {
      if (!res.ok) throw new Error("Cards JSON fetch failed: " + res.status);
      return res.json();
    })
    .then(data => {
      console.log("Loaded cards.json:", data);
      cards = [...data, ...data];
      shuffleCards();
      generateCards();
    })
    .catch(err => console.error("Error loading cards.json:", err));

  function shuffleCards() {
    let currentIndex = cards.length, randomIndex;
    while (currentIndex !== 0) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
      const tmp = cards[currentIndex];
      cards[currentIndex] = cards[randomIndex];
      cards[randomIndex] = tmp;
    }
  }

  function generateCards() {
    gridContainer.innerHTML = "";
    for (const card of cards) {
      console.log("creating card:", card.name, "->", card.image);
      const cardElement = document.createElement("div");
      cardElement.className = "card";
      cardElement.setAttribute("data-name", card.name);

      const front = document.createElement("div");
      front.className = "front";

      const img = document.createElement("img");
      img.className = "front-image";
      img.alt = card.name;
      img.src = card.image;

      img.onerror = () => {
        console.error(`Image failed to load: ${img.src} (check path & server root)`);
        img.style.opacity = "0.3";
      };

      front.appendChild(img);

      const back = document.createElement("div");
      back.className = "back";

      cardElement.appendChild(front);
      cardElement.appendChild(back);

      gridContainer.appendChild(cardElement);
      cardElement.addEventListener("click", flipCard);
    }
  }

  function flipCard() {
    if (lockBoard) return;
    if (this === firstCard) return;

    this.classList.add("flipped");

    if (!firstCard) {
      firstCard = this;
      return;
    }

    secondCard = this;
    score++;
    document.querySelector(".score").textContent = score;
    lockBoard = true;

    checkForMatch();
  }

  function checkForMatch() {
    const isMatch = firstCard.dataset.name === secondCard.dataset.name;
    if (isMatch) disableCards();
    else unflipCards();
  }

  function disableCards() {
    firstCard.removeEventListener("click", flipCard);
    secondCard.removeEventListener("click", flipCard);
    resetBoard();
  }

  function unflipCards() {
    setTimeout(() => {
      firstCard.classList.remove("flipped");
      secondCard.classList.remove("flipped");
      resetBoard();
    }, 1000);
  }

  function resetBoard() {
    firstCard = null;
    secondCard = null;
    lockBoard = false;
  }

  window.restart = function() {
    resetBoard();
    shuffleCards();
    score = 0;
    document.querySelector(".score").textContent = score;
    generateCards();
  };
});
