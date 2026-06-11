import random
import os
import textwrap

def generate_svg(quote):
    """Generates an SVG banner with the daily quote."""
    # Add quotes and wrap text to fit inside the SVG width
    wrapped_quote = textwrap.wrap(f'"{quote}"', width=45)
    
    line_height = 36
    num_lines = len(wrapped_quote)
    # Calculate starting Y to center the text vertically
    start_y = 150 - ((num_lines - 1) * line_height / 2)
    
    tspan_elements = ""
    for i, line in enumerate(wrapped_quote):
        y_pos = start_y + (i * line_height)
        tspan_elements += f'      <tspan x="50%" y="{y_pos}" text-anchor="middle">{line}</tspan>\n'

    svg_template = f"""<svg width="800" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .bg {{ fill: #0d1117; }}
      .border {{ stroke: #30363d; stroke-width: 1.5; rx: 12; ry: 12; fill: none; }}
      .title {{ font: 500 16px 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; fill: #8b949e; }}
      .quote {{ font: 400 24px 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; fill: #c9d1d9; font-style: italic; }}
      .footer {{ font: 400 13px 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; fill: #8b949e; }}
    </style>
  </defs>

  <rect width="100%" height="100%" class="bg" rx="12" ry="12"/>
  <rect width="100%" height="100%" class="border" />

  <text x="40" y="45" class="title">Daily Wisdom</text>

  <text x="50%" class="quote">
{tspan_elements.rstrip()}
  </text>

  <text x="40" y="270" class="footer">Raj • Updated Daily</text>
</svg>"""

    # Create assets directory if it doesn't exist
    os.makedirs('assets', exist_ok=True)
    
    # Save the SVG
    with open('assets/daily-wisdom.svg', 'w', encoding='utf-8') as f:
        f.write(svg_template)

def main():
    """Reads quotes, selects a random one, and generates the SVG."""
    quotes_file = 'quotes.txt'

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
    
    # Generate the SVG banner
    generate_svg(selected_quote)
    print("assets/daily-wisdom.svg generated successfully.")

if __name__ == '__main__':
    main()
