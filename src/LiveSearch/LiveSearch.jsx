import { useState, useEffect } from "react";
import { Search } from "lucide-react";

const sampleData = [
  "JavaScript",
  "Python",
  "C++",
  "Java",
  "Go",
  "Rust",
  "TypeScript",
  "Kotlin",
  "Swift",
  "Ruby",
  "PHP",
  "C#",
  "SQL",
  "HTML",
  "CSS",
  "React",
  "Next.js",
  "Node.js",
  "Express",
  "Django",
  "Flask",
  "Angular",
  "Vue",
  "Svelte",
  "Tailwind CSS",
];

const LiveSearch = () => {
  const [query, setQuery] = useState("");
  const [filteredResults, setFilteredResults] = useState([]);
  const [isFocused, setIsFocused] = useState(false);

  useEffect(() => {
    if (query.trim() === "") {
      setFilteredResults([]);
      return;
    }

    const results = sampleData.filter((item) =>
      item.toLowerCase().includes(query.toLowerCase())
    );
    setFilteredResults(results);
  }, [query]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-900 via-purple-900 to-indigo-900 flex flex-col items-center justify-center p-6">
      <div className="w-full max-w-md relative">
        <div className="flex items-center bg-white/10 backdrop-blur-lg border border-white/20 rounded-full px-4 py-2 shadow-lg focus-within:ring-2 focus-within:ring-purple-400 transition-all duration-300">
          <Search className="text-purple-300 w-5 h-5 mr-2" />
          <input
            type="text"
            placeholder="Search programming languages..."
            className="bg-transparent outline-none flex-1 text-white placeholder-gray-400"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onFocus={() => setIsFocused(true)}
            onBlur={() => setTimeout(() => setIsFocused(false), 150)}
          />
        </div>

        {/* Dropdown Suggestions */}
        {isFocused && filteredResults.length > 0 && (
          <ul className="absolute w-full mt-2 bg-white/10 backdrop-blur-md border border-white/20 rounded-xl shadow-xl overflow-hidden animate-fadeIn">
            {filteredResults.map((item, index) => (
              <li
                key={index}
                onClick={() => {
                  setQuery(item);
                  setFilteredResults([]);
                }}
                className="px-4 py-2 text-white hover:bg-purple-600 cursor-pointer transition-colors duration-200"
              >
                {item}
              </li>
            ))}
          </ul>
        )}

        {/* No Results */}
        {isFocused && query && filteredResults.length === 0 && (
          <div className="absolute w-full mt-2 bg-white/10 backdrop-blur-md border border-white/20 rounded-xl shadow-lg text-gray-300 px-4 py-2 text-center animate-fadeIn">
            No results found
          </div>
        )}
      </div>
    </div>
  );
};

// Simple animation
const style = document.createElement("style");
style.innerHTML = `
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-5px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fadeIn {
  animation: fadeIn 0.2s ease-in-out;
}
`;
document.head.appendChild(style);

export default LiveSearch;
