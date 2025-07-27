import React from "react";
import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Questions from "./pages/Questions";
import Answers from "./pages/Answers";

const routes = [
  { path: "/", element: <Home /> },
  { path: "/questions", element: <Questions /> },
  { path: "/answers", element: <Answers /> },
];

const App = () => {
  const pageNav = routes.map(
    (
      { path, element } //{ path, element } - .map((route, i) => …) gives (routeObject, index), not (path, element).
    ) => <Route key={path} path={path} element={element} />
  );

  return <Routes>{pageNav}</Routes>;
};

export default App;
