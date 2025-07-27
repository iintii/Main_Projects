import React, { useEffect, useState, useMemo } from "react";
import { useNavigate } from "react-router-dom";
import { fetchQuestions } from "../api/trivia";
import { decode } from "html-entities";
import manageOptions from "../manageOptions";
import clsx from "clsx";
import { shuffle } from "lodash";

const Questions = () => {
  const [questions, setQuestions] = useState([]);
  const [guessedOption, setGuessedOption] = useState({});
  const navigate = useNavigate();

  const allAnswered =
    questions.length > 0 &&
    Object.keys(guessedOption).length === questions.length;

  //add fetched array to questions
  useEffect(() => {
    fetchQuestions(5, "easy")
      .then((array) => {
        setQuestions(array);
      })
      .catch((err) => console.log(err));
  }, []);

  const optionsArr = useMemo(
    () => manageOptions(questions).map((option) => shuffle(option)),
    [questions]
  ); // is an array of arrays. use memo to store cache to "remember". shuffle only when questions change

  //iterate through answer options array

  //iterate through Questions array and through optArr
  const showQuestions = questions.map((obj, i) => {
    return (
      <article key={i}>
        <h2>{decode(obj.question)}</h2>

        {optionsArr[i] &&
          optionsArr[i].map((option, j) => {
            const isSelected = option === guessedOption[i];
            const bg = clsx({
              option: true,
              "option-selected": isSelected,
            });
            return (
              <label key={j} className={bg}>
                <input
                  onChange={() =>
                    setGuessedOption((prev) => ({ ...prev, [i]: option }))
                  }
                  type="radio"
                  name={`q${i}`}
                  value={option}
                  checked={isSelected}
                />
                {decode(option)}
              </label>
            );
          })}
      </article>
    );
  });

  function handleCheckAnswers() {
    const score = questions.reduce((acc, question, index) => {
      if (question.correct_answer === guessedOption[index]) {
        return acc + 1;
      }
      return acc;
    }, 0);
    navigate("/answers", { state: { score, total: questions.length } });
  }

  return (
    <main>
      {showQuestions}

      {allAnswered && (
        <button onClick={handleCheckAnswers}>Check Answers</button>
      )}
    </main>
  );
};

export default Questions;
