export default function IngredientList({ ingredients, getRecipe, loading }) {
  const formattedIngredients = ingredients.map((each) => (
    <li key={each}>{each}</li>
  ));

  return (
    <>
      <h1>Ingredients List</h1>
      <ul>{formattedIngredients}</ul>
      {ingredients.length > 3 && (
        <div className="ready-recipe">
          <h2>Ready for a recipe?</h2>
          <span>Generate a recipe from your ingredients list</span>
          <button onClick={getRecipe}>
            {loading ? "Loading..." : "Get a Recipe"}
          </button>
        </div>
      )}
    </>
  );
}
