import random
import datetime
import os
import textwrap

def generate_svg(quote):
    """Generates an SVG banner with the daily quote."""
    # Add quotes and wrap text to fit inside the SVG width
    wrapped_quote = textwrap.wrap(f'"{quote}"', width=45)
    
    line_height = 42
    num_lines = len(wrapped_quote)
    # Calculate starting Y to center the text vertically
    start_y = 200 - ((num_lines - 1) * line_height / 2)
    
    tspan_elements = ""
    for i, line in enumerate(wrapped_quote):
        y_pos = start_y + (i * line_height)
        tspan_elements += f'      <tspan x="50%" y="{y_pos}" text-anchor="middle">{line}</tspan>\n'

    svg_template = f"""<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .bg {{ fill: #0d1117; }}
      .border {{ stroke: #30363d; stroke-width: 2; rx: 12; ry: 12; fill: none; }}
      .title {{ font: 600 18px 'Segoe UI', Ubuntu, Sans-Serif; fill: #58a6ff; }}
      .quote {{ font: 400 28px 'Segoe UI', Ubuntu, Sans-Serif; fill: #c9d1d9; font-style: italic; }}
      .footer {{ font: 400 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: #8b949e; }}
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" rx="12" ry="12"/>
  <rect width="100%" height="100%" class="border" />

  <text x="40" y="50" class="title">Daily Wisdom</text>

  <text x="50%" class="quote">
{tspan_elements.rstrip()}
  </text>

  <text x="40" y="370" class="footer">Updated Daily</text>
</svg>"""

    # Create assets directory if it doesn't exist
    os.makedirs('assets', exist_ok=True)
    
    # Save the SVG
    with open('assets/daily-wisdom.svg', 'w', encoding='utf-8') as f:
        f.write(svg_template)

def update_readme():
    """Reads quotes, selects a random one, and updates the README.md and SVG."""
    quotes_file = 'quotes.txt'
    readme_file = 'README.md'

    try:
        with open(quotes_file, 'r', encoding='utf-8') as f:
            quotes = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: {quotes_file} not found.")
        return

    if not quotes:
        print("Error: No quotes found in the file.")
        return

    selected_quote = random.choice(quotes)
    today = datetime.date.today().isoformat()
    
    # Generate the SVG banner
    generate_svg(selected_quote)
    
    # Generate the new README content
    readme_content = f"""# Daily Wisdom

> {selected_quote}

---

Updated automatically every day.

Last refresh: {today}
"""

    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("README.md and assets/daily-wisdom.svg updated successfully.")

if __name__ == '__main__':
    update_readme()
