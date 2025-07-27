import { useState } from "react";
import Header from "./Header";
import Chips from "./Chips";
import { clsx } from "clsx";
import { languages } from "./languages";
import { words } from "./words";
import Confetti from "react-confetti";

export default function App() {
  const getRandomWord = () => {
    return words[Math.floor(Math.random() * words.length)];
  };

  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  const [currentword, setCurrentWord] = useState(() => getRandomWord());
  const [guessedLetters, setGuessedLetters] = useState([]);

  const wrongGuessCount = guessedLetters.filter(
    (letter) => !currentword.includes(letter)
  ).length;

  const isGameWon = currentword
    .split("")
    .every((letter) => guessedLetters.includes(letter));
  const isGameLost = wrongGuessCount > languages.length - 1;

  const addlettersinGuestLetter = (letter) => {
    setGuessedLetters((prevLetters) =>
      !prevLetters.includes(letter) ? [...prevLetters, letter] : prevLetters
    );
  };

  const renderGameStatus = () => {
    if (isGameWon) {
      return (
        <div className="win-banner">
          <h2>You Win!</h2>
          <span>Well done! 🎉</span>
        </div>
      );
    }

    if (isGameLost) {
      return (
        <div className="lose-banner">
          <h2>Game Over!</h2>
          <span>All Languages have passed away 😭</span>
        </div>
      );
    }
  };

  const SetNewGame = () => {
    setGuessedLetters([]);
    setCurrentWord(getRandomWord());
  };

  const letterElements = currentword.split("").map((letter, index) => {
    const shouldRevealLetter = guessedLetters.includes(letter); //show letters mechanism

    return (
      <span className="letter" key={index}>
        {shouldRevealLetter ? letter.toUpperCase() : ""}
      </span>
    );
  });

  const keyboardElements = alphabet.split("").map((letter, index) => {
    const isGuessed = guessedLetters.includes(letter);
    const isCorrect = isGuessed && currentword.includes(letter);
    const isWrong = isGuessed && !currentword.includes(letter);
    const className = clsx("key", {
      correct: isCorrect,
      wrong: isWrong,
    });

    return (
      <button
        className={className}
        key={index}
        onClick={() => addlettersinGuestLetter(letter)}
      >
        {letter.toUpperCase()}
      </button>
    );
  });

  return (
    <main>
      {isGameWon && <Confetti recycle={false} numberOfPieces={1000} />}

      <Header />
      <section className="game-status">{renderGameStatus()}</section>
      <Chips wrongGuessCount={wrongGuessCount} />
      <section className="word-display">{letterElements}</section>
      <section className="keyboard">{keyboardElements}</section>
      {isGameLost || isGameWon ? (
        <button className="new-game-btn" onClick={SetNewGame}>
          New Game
        </button>
      ) : undefined}
    </main>
  );
}
