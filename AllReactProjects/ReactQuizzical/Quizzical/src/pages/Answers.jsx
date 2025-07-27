import React from "react";
import { Link } from "react-router-dom";

export default function Answers() {
  // Note: Score logic will be handled from the Questions page.
  return (
    <main className="container">
      <h1>Quiz Results</h1>
      <p className="score">You scored 0/0 correct answers</p>
      <Link to="/questions">
        <button className="btn">Play Again</button>
      </Link>
      <Link to="/">
        <button className="btn btn-secondary">Back to Home</button>
      </Link>
    </main>
  );
}
