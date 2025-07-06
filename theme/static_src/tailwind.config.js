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
        // PRIMARY: Modern, professional orange (vibrant yet accessible)
        primary: {
          50: "#fff7ed", // Soft cream-orange
          100: "#ffedd5", // Light peach
          200: "#fed7aa", // Warm apricot
          300: "#fdba74", // Muted orange
          400: "#fb923c", // Vibrant orange (accent)
          500: "#f97316", // Primary brand orange (WCAG compliant)
          600: "#ea580c", // Deep orange (buttons/hover)
          700: "#c2410c", // Rich burnt orange
          800: "#9a3412", // Dark terracotta
          900: "#7c2d12", // Deep sophisticated orange
          DEFAULT: "#f97316", // Tailwind's default orange-500
        },

        // SECONDARY: Complementary blue (cool contrast)
        secondary: {
          50: "#f0f9ff", // Lightest sky blue
          100: "#e0f2fe", // Pale blue
          200: "#bae6fd", // Soft azure
          300: "#7dd3fc", // Light cerulean
          400: "#38bdf8", // Bright blue
          500: "#0ea5e9", // Balanced primary blue
          600: "#0284c7", // Strong cobalt
          700: "#0369a1", // Deep navy
          800: "#075985", // Dark navy
          900: "#0c4a6e", // Near-black blue
        },

        // Scrollbar (orange-tinged)
        scrollbar: {
          bg: "#fed7aa00", // Light orange transparent
          color: "#f9731661", // Primary orange with transparency
        },

        // Text colors (optimized contrast)
        text: {
          100: "#1e293b", // High-contrast slate (WCAG AAA)
          200: "#334155", // Secondary text
          300: "#64748b", // Tertiary text
          400: "#94a3b8", // Disabled text
        },

        // Backgrounds (warm neutrals)
        bg: {
          100: "#ffffff", // Pure white
          200: "#fef6e6", // Warm off-white
          300: "#f5f5f4", // Stone-50 (neutral)
          400: "#e7e5e4", // Light gray
          500: "#d6d3d1", // Medium gray
        },

        // Semantic colors (harmonized with palette)
        success: "#16a34a", // Emerald green
        warning: "#d97706", // Amber-600
        error: "#dc2626", // Red-600
        info: "#2563eb", // Blue-600

        // Light/dark theme variants
        light: {
          card: "#ffffff",
          background: "#fef6e6", // Warm white
          text: "#1e293b",
          border: "#e7e5e4", // Light gray
          glass: "rgba(255, 247, 237, 0.9)", // Warm glass
          overlay: "rgba(249, 115, 22, 0.08)", // Orange tint
        },
        dark: {
          card: "#1e293b", // Slate-800
          background: "#0f172a", // Slate-900 (deep navy)
          text: "#f8fafc",
          border: "#334155",
          glass: "rgba(30, 41, 59, 0.9)",
          overlay: "rgba(14, 165, 233, 0.08)", // Blue tint
        },
      },

      // Enhanced effects
      boxShadow: {
        glass: "0 4px 20px rgba(249, 115, 22, 0.1)", // Orange tint
        "glass-dark": "0 4px 20px rgba(14, 165, 233, 0.15)", // Blue tint
      },
      backdropBlur: {
        glass: "10px", // Modern blur strength
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
