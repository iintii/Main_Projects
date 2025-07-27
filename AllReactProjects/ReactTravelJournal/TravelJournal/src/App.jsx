import Header from "./Header";
import Entry from "./Entry";
import Data from "./data";

export default function App() {
  const travelElement = Data.map((element) => {
    return <Entry key={element.id} entry={element} />;
  });

  return (
    <>
      <Header />
      <main>{travelElement}</main>
    </>
  );
}
