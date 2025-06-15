# 🚀 Getting Started

> [!TIP]
> Welcome to this repository! Start by visiting [Templates.md](Templates.md) to explore all available **templates and themes**.

Once you've chosen a template that fits your style, follow these steps to set up your project:

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/madhurimarawat/Portfolio-Templates.git
   ```

2. Browse through the templates and decide which one you want to use.

3. Head over to the [Setup\_Files](Setup_Files) folder to **automatically configure your portfolio** using the provided scripts.

4. Local testing, customization, and setup instructions are clearly explained in that folder.

> [!NOTE]
> 💡 **[User Data Location](https://github.com/madhurimarawat/Portfolio-Templates/tree/main/assets/user_data)**
> All dynamic content (like social links and personal information) is managed through JSON files located in the [`assets/user_data/`](https://github.com/madhurimarawat/Portfolio-Templates/tree/main/assets/user_data) directory.

Each file is separated for modularity — for example:

* [`social_links.json`](https://github.com/madhurimarawat/Portfolio-Templates/blob/main/assets/user_data/social_links.json)
* [`user.json`](https://github.com/madhurimarawat/Portfolio-Templates/blob/main/assets/user_data/user.json)

You can either **manually edit these JSON files** or **use the automated setup scripts** in the [`Setup_Files`](https://github.com/madhurimarawat/Portfolio-Templates/tree/main/Setup_Files) folder to configure them.

🧠 **[Centralized Data Handling – `index.js`](https://github.com/madhurimarawat/Portfolio-Templates/blob/main/index.js)**

The file [`index.js`](https://github.com/madhurimarawat/Portfolio-Templates/blob/main/index.js) serves as the **central script** that fetches and distributes all user data across different templates and pages. This ensures consistency and simplifies updates across the project.

---

## 🌐 Hosting

This project is optimized for **GitHub Pages hosting**.
If you're using **Netlify**, **Vercel**, or another platform:

> [!WARNING]
> Be sure to **remove permalink settings** from individual pages in `_config.yml` or front matter to prevent routing issues.

If you encounter any issues while deploying or customizing, feel free to:

* 📂 [Open an Issue](https://github.com/madhurimarawat/Portfolio-Templates/issues)
* 💬 [Start a Discussion](https://github.com/madhurimarawat/Portfolio-Templates/discussions)

For contribution guidelines, please refer to:
🛠️ [CONTRIBUTING.md](https://github.com/madhurimarawat/Portfolio-Templates/blob/main/CONTRIBUTING.md)