module.exports = {
  darkMode: "class",
  content: [
    "../templates/**/*.html",
    "./flowbite/**/*.js",
    "../../templates/**/*.html",
    "../../**/templates/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        // Primary color scale
        primary: {
          50: "#eff6ff",
          100: "#dbeafe",
          200: "#bfdbfe",
          300: "#93c5fd",
          400: "#60a5fa",
          500: "#3b82f6",
          600: "#2563eb",
          700: "#1d4ed8",
          800: "#1e40af",
          900: "#1e3a8a",
          DEFAULT: "#2563eb",
        },

        // Theme-specific colors
        light: {
          card: "#ffffff",
          background: "#f8fafc",
          text: "#1e293b",
          border: "#e2e8f0",
          glass: "rgba(255, 255, 255, 0.7)",
        },
        dark: {
          card: "#1e293b",
          background: "#0f172a",
          text: "#e2e8f0",
          border: "#334155",
          glass: "rgba(30, 41, 59, 0.7)",
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
