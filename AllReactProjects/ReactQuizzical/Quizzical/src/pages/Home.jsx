import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <main>
      <h1>Quizzical Trivia</h1>
      <p>Are you more knowledgable than you look? Find out now!</p>
      <Link to="/questions">
        <button>Start Quiz</button>
      </Link>
    </main>
  );
};

export default Home;
