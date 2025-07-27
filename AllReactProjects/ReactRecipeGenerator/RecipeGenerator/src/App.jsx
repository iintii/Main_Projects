import ClaudeRecipe from "./component/ClaudeRecipe";
import IngredientList from "./component/IngredientList";
import Header from "./Header";
import { useState } from "react";
import { getRecipeFromHuggingFace } from "./ai";

export default function App() {
  const [ingredients, setIngredients] = useState([]);
  const [recipe, setRecipe] = useState("");
  const [loading, setLoading] = useState(false);

  const addIngredient = (formData) => {
    const data = formData.get("ingredients");
    {
      data && data.trim() !== "" //only add non empty and non white space ingredients
        ? setIngredients((prev) => [...prev, data])
        : null;
    }
  };

  async function getRecipe() {
    setLoading(true);
    const recipeMarkdown = await getRecipeFromHuggingFace(ingredients);
    setRecipe(recipeMarkdown);
    setLoading(false);
  }

  return (
    <>
      <Header />

      <div className="form-container">
        <form action={addIngredient}>
          <input type="text" name="ingredients" placeholder="e.g. oregano" />
          <button>Add Ingredient</button>
        </form>
      </div>

      {ingredients.length > 0 ? (
        <div className="ready-container">
          <IngredientList
            loading={loading}
            ingredients={ingredients}
            getRecipe={getRecipe}
          />
        </div>
      ) : undefined}

      {recipe ? (
        <div className="reply-container">
          <ClaudeRecipe recipe={recipe} />
        </div>
      ) : null}
    </>
  );
}
