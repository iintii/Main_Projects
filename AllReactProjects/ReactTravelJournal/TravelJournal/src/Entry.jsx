export default function Entry(props) {
  return (
    <>
      <article className="journal-entry">
        <div className="main-image-container">
          <img src={props.entry.img.src} alt={props.entry.img.alt} />
        </div>
        <div>
          <img src=".\src\assets\Fill 219.png" alt="marker" />
          <span>{props.entry.country}</span>
          <a href={props.entry.googleMapsLink}>Map Link</a>
          <h2>{props.entry.title}</h2>
          <p>{props.entry.dates}</p>
          <p>{props.entry.text}</p>
        </div>
      </article>
      <hr />
    </>
  );
}
