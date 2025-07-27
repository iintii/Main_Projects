import { useState } from "react";
import Die from "./Die";
import { nanoid } from "nanoid";
import Confetti from "react-confetti";

export default function App() {
  const [count, setCount] = useState(0);

  const counter = () => {
    !gameWon ? setCount((p) => p + 1) : setCount(0);
  };

  const generateDiceObjects = () => {
    return new Array(10).fill(0).map(() => ({
      value: Math.ceil(Math.random() * 6),
      isHeld: false,
      id: nanoid(),
    }));
  };

  const [dice, setDice] = useState(generateDiceObjects());

  const holdDie = (id) => {
    setDice((prev) =>
      prev.map((obj) => (id == obj.id ? { ...obj, isHeld: !obj.isHeld } : obj))
    );
  };

  const rollDice = () => {
    if (!gameWon) {
      setDice((prev) =>
        prev.map((obj) =>
          obj.isHeld ? obj : { ...obj, value: Math.ceil(Math.random() * 6) }
        )
      );
    } else {
      setDice(generateDiceObjects());
    }
  };

  const gameWon = dice.every(
    (obj) => obj.isHeld && obj.value === dice[0].value
  );

  const eachDie = (
    <div className="dice-container">
      {dice.map((obj) => (
        <Die dice={obj} hold={holdDie} key={obj.id} />
      ))}
    </div>
  );

  return (
    <>
      {gameWon && (
        <Confetti
          width={window.innerWidth}
          height={window.innerHeight}
          numberOfPieces={250}
          recycle={false}
          gravity={0.25}
        />
      )}
      <main>
        <h1 className="tenzies-title">Tenzies</h1>
        {eachDie}
        <h1 className="roll-count">{count}</h1>
        <p className="tenzies-desc">
          Roll until all dice are the same. Click each die to freeze it at its
          current value.
        </p>
      </main>
      <div className="button-row">
        <button
          className="roll-btn"
          onClick={() => {
            rollDice();
            counter();
          }}
        >
          {gameWon ? "New Game" : "Roll"}
        </button>
        <button
          className="reset-btn"
          onClick={() => {
            setCount(0);
            setDice(generateDiceObjects());
          }}
        >
          Reset
        </button>
      </div>
    </>
  );
}
