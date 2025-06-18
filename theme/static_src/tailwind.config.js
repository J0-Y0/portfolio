/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class", // Add this line to enable class-based dark mode

  content: [
    "../templates/**/*.html",
    ".//flowbite/**/*.js",
    "../../templates/**/*.html",
    "../../**/templates/**/*.html",
    "../../**/templates/*.html",
  ],
  theme: {
    extend: {
      colors: {
        // Add light mode colors
        light: {
          primary: "#1a73e8",
          secondary: "#fbbc05",
          background: "#ffffff",
          text: "#202124",
          card: "#f8f9fa",
          border: "#dadce0",
        },
        // Your existing dark colors (renamed for clarity)
        dark: {
          primary: "#147294",
          secondary: "#F4C236",
          background: "#0D1F2D",
          text: "#E6E6E6",
          card: "#1A202C",
          border: "#2c4558",
        },
      },
    },
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/aspect-ratio"),
    require("flowbite/plugin"),
  ],
};
