import ReactMarkdown from "react-markdown";

export default function ClaudeRecipe({ recipe }) {
  return (
    <section>
      <h2>Chef AI recommends:</h2>
      <ReactMarkdown>{recipe}</ReactMarkdown>
    </section>
  );
}
