export default function Die({ hold, dice }) {
  return (
    <button
      className={`die-btn${dice.isHeld ? " held" : ""}`}
      onClick={() => {
        hold(dice.id);
      }}
    >
      {dice.value}
    </button>
  );
}
