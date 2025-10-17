function generatePalette() {
  const palette = document.getElementById("palette");
  palette.innerHTML = "";

  for (let i = 0; i < 3; i++) {
    const color = "#" + Math.floor(Math.random() * 16777215).toString(16);
    const box = document.createElement("div");
    box.classList.add("color-box");
    box.style.backgroundColor = color;
    box.title = color;
    box.addEventListener("click", () => {
      navigator.clipboard.writeText(color);
      alert(`Copied ${color} to clipboard!`);
    });
    palette.appendChild(box);
  }
}

document.getElementById("generate").addEventListener("click", generatePalette);
generatePalette();
