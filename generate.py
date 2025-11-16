#!/usr/bin/env python3
"""
FRC Team Robot Card Generator
Reads YAML files from cards/ directory and generates an HTML gallery.
"""

import os
import yaml
from pathlib import Path
from jinja2 import Template

# HTML template with embedded CSS
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Team 4419 Rewind - Robot Design Gallery</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="../assets/style.css">
    <style>
        body {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            padding: 2rem 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        .header {
            text-align: center;
            color: #fff;
            margin-bottom: 3rem;
            padding: 2rem;
        }
        .header h1 {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }
        .header p {
            font-size: 1.2rem;
            color: #a8b2d1;
        }
        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
        }
        .robot-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }
        .robot-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
            border-color: rgba(102, 126, 234, 0.5);
        }
        .robot-card h2 {
            color: #667eea;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        .robot-card .username {
            color: #a8b2d1;
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
        }
        .robot-card .year-badge {
            display: inline-block;
            background: rgba(102, 126, 234, 0.2);
            color: #667eea;
            padding: 0.25rem 0.75rem;
            border-radius: 12px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        .ascii-art {
            background: rgba(0, 0, 0, 0.3);
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            border-left: 3px solid #667eea;
        }
        .ascii-art pre {
            color: #64ffda;
            font-family: 'Courier New', monospace;
            font-size: 0.85rem;
            margin: 0;
            line-height: 1.4;
        }
        .mechanism {
            color: #e6f1ff;
            font-weight: 500;
            margin-bottom: 1rem;
            padding-left: 1rem;
            border-left: 2px solid rgba(100, 255, 218, 0.3);
        }
        .why-cool, .design-philosophy {
            color: #a8b2d1;
            font-size: 0.95rem;
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        .section-label {
            color: #64ffda;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        .footer {
            text-align: center;
            color: #a8b2d1;
            margin-top: 4rem;
            padding: 2rem;
            font-size: 0.9rem;
        }
        @media (max-width: 768px) {
            .card-grid {
                grid-template-columns: 1fr;
            }
            .header h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Team 4419 Rewind - Robot Design Gallery</h1>
        <p>Student Dream Robots & Design Philosophies</p>
    </div>

    <div class="card-grid">
        {% for card in cards %}
        <div class="robot-card">
            <h2>{{ card.robot_name }}</h2>
            <div class="username">@{{ card.username }}</div>
            <span class="year-badge">{{ card.year }} Season</span>

            <div class="ascii-art">
                <pre>{{ card.ascii_art }}</pre>
            </div>

            <div class="section-label">Signature Mechanism</div>
            <div class="mechanism">{{ card.signature_mechanism }}</div>

            <div class="section-label">Why It's Cool</div>
            <div class="why-cool">{{ card.why_cool }}</div>

            <div class="section-label">Design Philosophy</div>
            <div class="design-philosophy">{{ card.design_philosophy }}</div>
        </div>
        {% endfor %}
    </div>

    <div class="footer">
        <p>Generated by Team 4419 Robot Card Generator</p>
        <p>{{ cards|length }} robot design{{ 's' if cards|length != 1 else '' }} created by our amazing team!</p>
    </div>
</body>
</html>
"""


def load_cards(cards_dir='cards'):
    """Load all YAML card files from the cards directory."""
    cards = []
    cards_path = Path(cards_dir)

    if not cards_path.exists():
        print(f"Error: {cards_dir}/ directory not found!")
        return cards

    yaml_files = sorted(cards_path.glob('*.yaml'))

    for yaml_file in yaml_files:
        # Skip the template file
        if yaml_file.name == 'template.yaml':
            continue

        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                card_data = yaml.safe_load(f)

                # Validate required fields
                required_fields = ['username', 'robot_name', 'year', 'signature_mechanism',
                                 'ascii_art', 'why_cool', 'design_philosophy']

                missing_fields = [field for field in required_fields if field not in card_data]
                if missing_fields:
                    print(f"Warning: {yaml_file.name} is missing fields: {missing_fields}")
                    continue

                cards.append(card_data)
                print(f"✓ Loaded: {yaml_file.name}")

        except yaml.YAMLError as e:
            print(f"Error parsing {yaml_file.name}: {e}")
        except Exception as e:
            print(f"Error reading {yaml_file.name}: {e}")

    return cards


def generate_html(cards, output_file='generated/index.html'):
    """Generate HTML gallery from card data."""
    template = Template(HTML_TEMPLATE)
    html_content = template.render(cards=cards)

    # Ensure output directory exists
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write HTML file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✓ Generated: {output_file}")
    return output_path


def main():
    print("=" * 60)
    print("FRC Team 4419 - Robot Card Generator")
    print("=" * 60)
    print()

    # Load all cards
    cards = load_cards()

    if not cards:
        print("\n⚠ No valid robot cards found!")
        print("Make sure you have .yaml files in the cards/ directory.")
        return

    print(f"\nFound {len(cards)} robot card(s)")

    # Generate HTML
    output_path = generate_html(cards)

    print("\n" + "=" * 60)
    print(f"Success! {len(cards)} card(s) generated.")
    print(f"Open {output_path} in your browser to view the gallery!")
    print("=" * 60)


if __name__ == '__main__':
    main()
