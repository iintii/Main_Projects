import clsx from "clsx";
import { languages } from "./languages";

export default function Chips({ wrongGuessCount }) {
  const languageElements = languages.map((obj, index) => {
    const lostLanguages = index < wrongGuessCount;
    const className = clsx("chip", lostLanguages && "lost"); //base class chip is applied. condition: if lostlang true, "chip lost" is applied

    return (
      <span
        className={className}
        key={obj.name}
        style={{ background: obj.backgroundColor, color: obj.color }}
      >
        {obj.name}
      </span>
    );
  });
  return <section className="chips">{languageElements}</section>;
}
