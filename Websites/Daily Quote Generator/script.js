const quoteText = document.getElementById("quote-text");
const quoteAuthor = document.getElementById("quote-author");

let lastIndex = -1;

const quotes = [
    { text: "The best way to predict the future is to invent it.", author: "Alan Kay" },
    { text: "Life is 10% what happens to us and 90% how we react to it.", author: "Charles R. Swindoll" },
    { text: "In the middle of every difficulty lies opportunity.", author: "Albert Einstein" },
    { text: "Do what you can, with what you have, where you are.", author: "Theodore Roosevelt" },
    { text: "It always seems impossible until it’s done.", author: "Nelson Mandela" },
    { text: "If you want to lift yourself up, lift up someone else.", author: "Booker T. Washington" },
    { text: "Believe you can and you're halfway there.", author: "Theodore Roosevelt" },
    { text: "Success is not final, failure is not fatal. It is the courage to continue that counts.", author: "Winston Churchill" },
    { text: "The only way to do great work is to love what you do.", author: "Steve Jobs" },
    { text: "Start where you are. Use what you have. Do what you can.", author: "Arthur Ashe" },
    { text: "Don't watch the clock. Do what it does. Keep going.", author: "Sam Levenson" },
    { text: "Keep your face always toward the sunshine and shadows will fall behind you.", author: "Walt Whitman" },
    { text: "Everything you’ve ever wanted is on the other side of fear.", author: "George Addair" },
    { text: "Hardships often prepare ordinary people for an extraordinary destiny.", author: "C.S. Lewis" },
    { text: "Whether you think you can or think you can’t, you’re right.", author: "Henry Ford" },
    { text: "Act as if what you do makes a difference. It does.", author: "William James" },
    { text: "Quality means doing it right when no one is looking.", author: "Henry Ford" },
    { text: "The future depends on what you do today.", author: "Mahatma Gandhi" },
    { text: "You miss 100% of the shots you don’t take.", author: "Wayne Gretzky" },
    { text: "Opportunities don't happen. You create them.", author: "Chris Grosser" }
];

function showRandomQuote() {
    if (quotes.length === 0) return;
    let index;
    do {
        index = Math.floor(Math.random() * quotes.length);
    } while (index === lastIndex && quotes.length > 1);
    lastIndex = index;

    const quote = quotes[index];

    setTimeout(() => {
        quoteText.textContent = `"${quote.text}"`;
        quoteAuthor.textContent = `– ${quote.author}`;
    });
}

document.addEventListener("keydown", (event) => {
    if (event.code === "Space") {
        showRandomQuote();
    }});

showRandomQuote();