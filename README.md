# 📊 BADASS™ Intl WhatsApp Stats Dashboard

Live statistics dashboard for tracking WhatsApp group activity!

## 🚀 Quick Start

### Option 1: Visit Live Dashboard (Recommended)
Just go to: **https://YOUR_USERNAME.github.io/whatsapp-stats-dashboard/**

Then drag & drop your ChatStats HTML export to update!

### Option 2: Run Locally
```bash
# Just open index.html in your browser
open index.html
# or
python3 -m http.server 8000
# then visit http://localhost:8000
```

## 📱 How to Update Stats

### Method A: Drag & Drop (Easiest!)
1. Export chat from ChatStats app
2. Open the dashboard
3. Drag & drop the HTML file
4. Done! ✨

### Method B: Using Scripts

**Windows:**
```batch
update.bat "C:\path\to\ChatStats_export.html"
```

**Mac/Linux:**
```bash
./update.sh /path/to/ChatStats_export.html
```

This will:
- Parse the HTML file
- Generate `stats.json`
- Update `README.md`
- Show summary statistics

Then push to GitHub:
```bash
git add .
git commit -m "Update stats"
git push
```

## 📁 Files in This Folder

- **index.html** - The main dashboard (DO NOT DELETE!)
- **stats.json** - Latest statistics data (optional, for pre-loading)
- **update_stats.py** - Python script to process ChatStats exports
- **update.bat** - Windows batch script
- **update.sh** - Unix shell script
- **SETUP_GUIDE.md** - Complete setup instructions
- **.gitignore** - Prevents committing sensitive data

## 🔒 Important Security Notes

⚠️ **NEVER commit ChatStats HTML exports to GitHub!**

The `.gitignore` file is configured to block `.html` files by default. The HTML exports contain your private chat messages!

Safe to commit:
- ✅ `index.html` (the dashboard itself)
- ✅ `stats.json` (just numbers, no messages)
- ✅ `README.md` (just text)
- ✅ Python scripts

DO NOT commit:
- ❌ ChatStats exports (*.html except index.html)
- ❌ Any files with actual messages

## 🎨 Customization

Edit `index.html` to change:
- Group name (line 46)
- Colors (CSS gradients)
- Activity thresholds
- Chart types

## 📊 Understanding the Stats

- **🔥 Top Contributors** (>30 msgs/day)
- **💪 Active** (15-30 msgs/day)
- **👍 Moderate** (5-15 msgs/day)
- **😐 Low** (1-5 msgs/day)
- **💤 Slackers** (<1 msg/day)

## 🐛 Troubleshooting

**Dashboard not loading?**
- Clear browser cache
- Check GitHub Pages is enabled
- Wait 2-3 minutes after pushing changes

**Upload not working?**
- Must be `.html` file from ChatStats
- Try a different browser
- Check browser console (F12) for errors

**Stats look wrong?**
- Re-export from ChatStats
- Make sure file is recent
- Check all members are included

## 🔗 Useful Links

- [Full Setup Guide](SETUP_GUIDE.md)
- [GitHub Pages Documentation](https://pages.github.com/)
- [ChatStats App](https://play.google.com/store/apps/details?id=com.joseluisgalan.android.chatstats)

## 💡 Tips

1. Export chat weekly to track trends
2. Bookmark the dashboard on mobile
3. Share with group members for motivation
4. Screenshot leaderboard for group chat
5. Use automation scripts for hands-free updates

## 🤝 Contributing

Found a bug? Have ideas? Open an issue or PR!

Ideas for improvements:
- Historical data tracking
- Trend analysis
- Export to PDF
- More chart types
- Mobile app

## 📄 License

MIT License - Free to use and modify!

---

**Made with 💜 and lots of spam**

Last Updated: February 22, 2026
