#!/usr/bin/env python3
"""
WhatsApp Group Stats - Automated Dashboard Updater
This script processes ChatStats HTML exports and generates data for the live dashboard
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

def parse_chatstats_html(html_file_path):
    """Parse ChatStats HTML export and extract user statistics"""
    
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract messages per user
    messages_section = html_content[
        html_content.find("id='num_mensajes'"):
        html_content.find("id='num_palabras'")
    ]
    messages_matches = re.findall(r"<span class='dato'>(\d+) : ([^<]+)</span>", messages_section)
    
    messages_data = {}
    for match in messages_matches:
        count = int(match[0])
        username = match[1].strip()
        messages_data[username] = count
    
    # Extract first message dates
    first_msg_section = html_content[
        html_content.find("id='primer_mensaje'"):
        html_content.find("id='ultimo_mensaje'")
    ]
    
    first_message_dates = {}
    for match in re.findall(r"(\d{2}/\d{2}/\d{4}) \d{2}:\d{2}.*?<span class='dato'>([^<]+)</span>", 
                           first_msg_section, re.DOTALL):
        date_str = match[0]
        username = match[1].strip()
        first_message_dates[username] = date_str
    
    # Calculate statistics
    today = datetime.now()
    members = []
    
    for username in messages_data:
        if username in first_message_dates:
            total_messages = messages_data[username]
            first_date_str = first_message_dates[username]
            
            # Parse date (DD/MM/YYYY)
            day, month, year = map(int, first_date_str.split('/'))
            first_date = datetime(year, month, day)
            
            days_active = (today - first_date).days + 1
            avg_per_day = total_messages / days_active
            
            members.append({
                'username': username,
                'totalMessages': total_messages,
                'daysActive': days_active,
                'avgPerDay': round(avg_per_day, 2),
                'firstDate': first_date_str
            })
    
    # Sort by average messages per day
    members.sort(key=lambda x: x['avgPerDay'], reverse=True)
    
    return {
        'members': members,
        'totalMessages': sum([m['totalMessages'] for m in members]),
        'timestamp': datetime.now().isoformat(),
        'generatedAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

def generate_stats_json(data, output_path):
    """Generate JSON file for the dashboard"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Stats JSON generated: {output_path}")

def generate_readme(members, output_path):
    """Generate a README with current stats"""
    top_3 = members[:3]
    bottom_3 = members[-3:]
    
    readme_content = f"""# 📊 BADASS™ Intl WhatsApp Group Stats

## 🏆 Current Leaderboard

### Top 3 Contributors
1. **{top_3[0]['username']}** - {top_3[0]['avgPerDay']:.2f} msgs/day 🔥
2. **{top_3[1]['username']}** - {top_3[1]['avgPerDay']:.2f} msgs/day 🔥
3. **{top_3[2]['username']}** - {top_3[2]['avgPerDay']:.2f} msgs/day 💪

### Bottom 3 Slackers
{len(members)-2}. **{bottom_3[0]['username']}** - {bottom_3[0]['avgPerDay']:.2f} msgs/day 😐
{len(members)-1}. **{bottom_3[1]['username']}** - {bottom_3[1]['avgPerDay']:.2f} msgs/day 💤
{len(members)}. **{bottom_3[2]['username']}** - {bottom_3[2]['avgPerDay']:.2f} msgs/day 💤

## 📈 Activity Levels

- 🔥 **Top Contributors** (>30 msgs/day): {len([m for m in members if m['avgPerDay'] > 30])} members
- 💪 **Active** (15-30 msgs/day): {len([m for m in members if 15 <= m['avgPerDay'] <= 30])} members
- 👍 **Moderate** (5-15 msgs/day): {len([m for m in members if 5 <= m['avgPerDay'] < 15])} members
- 😐 **Low** (1-5 msgs/day): {len([m for m in members if 1 <= m['avgPerDay'] < 5])} members
- 💤 **Slackers** (<1 msg/day): {len([m for m in members if m['avgPerDay'] < 1])} members

## 📊 Group Statistics

- **Total Messages:** {sum([m['totalMessages'] for m in members]):,}
- **Active Members:** {len(members)}
- **Spam Ratio:** {members[0]['avgPerDay'] / members[-1]['avgPerDay']:.1f}x (Top vs Bottom)

---

*Last Updated: {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}*

[View Live Dashboard](https://YOUR_USERNAME.github.io/whatsapp-stats-dashboard/)
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ README generated: {output_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_stats.py <path_to_chatstats_html>")
        print("\nExample:")
        print("  python update_stats.py ChatStats_export.html")
        sys.exit(1)
    
    html_file = sys.argv[1]
    
    if not Path(html_file).exists():
        print(f"❌ Error: File not found: {html_file}")
        sys.exit(1)
    
    print("🔄 Processing ChatStats HTML file...")
    
    try:
        # Parse the HTML file
        data = parse_chatstats_html(html_file)
        
        # Create output directory if it doesn't exist
        output_dir = Path('dashboard')
        output_dir.mkdir(exist_ok=True)
        
        # Generate stats JSON
        generate_stats_json(data, output_dir / 'stats.json')
        
        # Generate README
        generate_readme(data['members'], Path('README.md'))
        
        print("\n✨ Success! Dashboard updated successfully!")
        print(f"\n📈 Summary:")
        print(f"   Total Messages: {data['totalMessages']:,}")
        print(f"   Active Members: {len(data['members'])}")
        print(f"   Top Contributor: {data['members'][0]['username']} ({data['members'][0]['avgPerDay']:.2f} msgs/day)")
        print(f"\n🚀 You can now push these changes to GitHub!")
        
    except Exception as e:
        print(f"❌ Error processing file: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
