/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
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
        // Base colors (available in both modes)
        primary: "#147294",
        secondary: "#F4C236",
        tertiary: "#E6E6E6",
        quaternary: "#1A202C",

        // Light mode colors
        light: "#f8f9fa", // This replaces your light.bg
        lightcard: "#ffffff",
        lighttext: "#202124",

        // Dark mode colors
        dark: {
          bg: "#1A202C",
          card: "#0D1F2D",
          text: "#E6E6E6",
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
