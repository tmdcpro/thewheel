# The Wheel - 2 Minute Demo Script

## 🎬 **Demo Video Script** (120 seconds)

### **[0:00-0:15] Hook & Problem** (15 seconds)
**Screen**: Terminal with project directory
**Narration**: 
> "How many times have you started building something, only to discover it already exists? Meet The Wheel - an AI research engine that maps competitive landscapes before you code."

**Action**: Show project structure briefly

### **[0:15-0:45] Live Research Demo** (30 seconds)
**Screen**: Terminal
**Narration**: 
> "Let's research machine learning frameworks. Watch as The Wheel searches GitHub, analyzes projects, and maps relationships."

**Commands to run**:
```bash
source venv/bin/activate
PYTHONPATH=. python src/main.py "machine learning frameworks" --mock --limit 5
```

**Show**: Real-time output with project analysis

### **[0:45-1:15] Interactive Visualization** (30 seconds)
**Screen**: Browser with standalone_demo.html
**Narration**: 
> "Here's the magic - an interactive network showing TensorFlow, Hugging Face, and other frameworks. Blue nodes are projects, click to open GitHub. Drag to explore relationships."

**Actions**: 
- Click on TensorFlow node (opens GitHub)
- Drag nodes around
- Show relationship connections

### **[1:15-1:45] AI Agent Integration** (30 seconds)
**Screen**: Terminal showing MCP test
**Narration**: 
> "But it gets better. The Wheel integrates with AI agents through MCP protocol. Any AI agent can now do competitive research automatically."

**Commands**:
```bash
./test_mcp.sh
```

**Show**: MCP server responding with formatted research results

### **[1:45-2:00] Value Proposition & CTA** (15 seconds)
**Screen**: GitHub repository page
**Narration**: 
> "Stop reinventing the wheel. Map the landscape first. The Wheel is open source and ready to use. Link in description."

**Show**: GitHub repo with stars/forks, README preview

---

## 🎥 **Recording Setup Instructions**

### **Preparation** (5 minutes):
1. **Clean terminal**: Clear history, set up clean prompt
2. **Browser setup**: Open standalone_demo.html in new tab
3. **Test commands**: Run through script once to ensure timing
4. **Screen recording**: Use OBS, QuickTime, or similar (1080p recommended)

### **Pro Tips**:
- **Record in segments**: Easier to edit than one take
- **Use zoom**: Make terminal text clearly readable
- **Smooth mouse movements**: Slow, deliberate clicks and drags
- **Background music**: Optional light tech music
- **Captions**: Consider adding for accessibility

### **Quick Recording Commands**:
```bash
# Terminal segment
source venv/bin/activate
PYTHONPATH=. python src/main.py "machine learning frameworks" --mock --limit 5

# MCP segment  
./test_mcp.sh

# Open visualization
open standalone_demo.html
```

### **Editing Notes**:
- **Cut loading pauses**: Speed up or cut waiting time
- **Highlight clicks**: Add cursor highlights for clarity
- **Smooth transitions**: Quick fades between segments
- **End screen**: GitHub repo URL clearly visible

---

## 📱 **Alternative: Screen Recording Tools**

### **macOS**: 
```bash
# Built-in screen recording
# Cmd+Shift+5 → Select area → Record
```

### **Linux**:
```bash
# Install OBS Studio
sudo apt install obs-studio

# Or use built-in tools
gnome-screenshot --area
```

### **Windows**:
```bash
# Windows Game Bar
# Win+G → Record
```

---

**Total prep time**: ~10 minutes
**Recording time**: ~5 minutes (multiple takes)
**Editing time**: ~15 minutes

**Result**: Professional 2-minute demo showcasing all key features!
