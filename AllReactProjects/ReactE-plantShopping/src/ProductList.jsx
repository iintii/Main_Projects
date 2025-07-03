import React, { useState, useEffect } from "react";
import "./ProductList.css";
import CartItem from "./CartItem";
import { plantsArray } from "./plantData";
import { addItem, removeItem } from "./CartSlice";
import { useSelector, useDispatch } from "react-redux";

function ProductList({ onHomeClick }) {
  const [showCart, setShowCart] = useState(false);
  const [showPlants, setShowPlants] = useState(false); // State to control the visibility of the About Us page
  const [addToCart, setAddToCart] = useState({});
  const dispatch = useDispatch();
  const CartItems = useSelector((state) => state.cart.items);

  const calculateTotalQuantity = () => {
    return CartItems
      ? CartItems.reduce((total, item) => total + item.quantity, 0)
      : 0;
  };

  function handleAddtoCart(currentPlantInfo) {
    const isAdded = addToCart[currentPlantInfo.name];
    if (isAdded) {
      dispatch(removeItem(currentPlantInfo.name));
      setAddToCart((prev) => ({ ...prev, [currentPlantInfo.name]: false }));
    } else {
      dispatch(addItem(currentPlantInfo));
      setAddToCart((prev) => ({ ...prev, [currentPlantInfo.name]: true }));
    }
  }

  const allPlants = plantsArray.flatMap((category) => category.plants);
  const allCategories = plantsArray.flatMap((cat) => cat.category);
  const PlantCards = allPlants.map((plant, i) => {
    const isAdded = addToCart[plant.name];
    return (
      <div key={plant.name + i} className="product-card">
        <h3 className="product-title">{plant.className}</h3>
        <img className="product-image" src={plant.image} alt={plant.name} />
        <span className="product-price">{plant.cost}</span>
        <p>{plant.description}</p>
        <button
          className={`product-button${isAdded ? " added-to-cart" : ""}`}
          onClick={() => handleAddtoCart(plant)}
        >
          {isAdded ? "Added to Cart" : "Add to Cart"}
        </button>
      </div>
    );
  });

  const styleObj = {
    backgroundColor: "#4CAF50",
    color: "#fff!important",
    padding: "15px",
    display: "flex",
    justifyContent: "space-between",
    alignIems: "center",
    fontSize: "20px",
  };
  const styleObjUl = {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    width: "1100px",
  };
  const styleA = {
    color: "white",
    fontSize: "30px",
    textDecoration: "none",
  };

  const handleHomeClick = (e) => {
    e.preventDefault();
    onHomeClick();
  };

  const handleCartClick = (e) => {
    e.preventDefault();
    setShowCart(true); // Set showCart to true when cart icon is clicked
  };
  const handlePlantsClick = (e) => {
    e.preventDefault();
    setShowPlants(true); // Set showAboutUs to true when "About Us" link is clicked
    setShowCart(false); // Hide the cart when navigating to About Us
  };

  const handleContinueShopping = (e) => {
    e.preventDefault();
    setShowCart(false);
  };
  return (
    <div>
      <div className="navbar" style={styleObj}>
        <div className="tag">
          <div className="luxury">
            <img
              src="https://cdn.pixabay.com/photo/2020/08/05/13/12/eco-5465432_1280.png"
              alt=""
            />
            <a href="/" onClick={(e) => handleHomeClick(e)}>
              <div>
                <h3 style={{ color: "white" }}>Paradise Nursery</h3>
                <i style={{ color: "white" }}>Where Green Meets Serenity</i>
              </div>
            </a>
          </div>
        </div>
        <div style={styleObjUl}>
          <div>
            {" "}
            <a href="#" onClick={(e) => handlePlantsClick(e)} style={styleA}>
              Plants
            </a>
          </div>
          <div>
            {" "}
            <a href="#" onClick={(e) => handleCartClick(e)} style={styleA}>
              <h1 className="cart">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 256 256"
                  id="IconChangeColor"
                  height="68"
                  width="68"
                >
                  <rect width="156" height="156" fill="none"></rect>
                  <circle cx="80" cy="216" r="12"></circle>
                  <circle cx="184" cy="216" r="12"></circle>
                  <path
                    d="M42.3,72H221.7l-26.4,92.4A15.9,15.9,0,0,1,179.9,176H84.1a15.9,15.9,0,0,1-15.4-11.6L32.5,37.8A8,8,0,0,0,24.8,32H8"
                    fill="none"
                    stroke="#faf9f9"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    id="mainIconPathAttribute"
                  ></path>
                </svg>
                <span className="cart_quantity_count">
                  {calculateTotalQuantity()}
                </span>
              </h1>
            </a>
          </div>
        </div>
      </div>
      {!showCart ? (
        <div className="product-grid">
          <div className="product-list">{PlantCards}</div>
        </div>
      ) : (
        <CartItem onContinueShopping={handleContinueShopping} />
      )}
    </div>
  );
}

export default ProductList;
