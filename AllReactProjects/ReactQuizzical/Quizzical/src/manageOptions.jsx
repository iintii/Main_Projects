export default function manageOptions(questions) {
  const addOptionsToArray = questions.map(
    ({ correct_answer, incorrect_answers }) => {
      const optionsArr = [...incorrect_answers, correct_answer];
      return optionsArr;
    }
  );
  return addOptionsToArray;
}
