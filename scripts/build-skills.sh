#!/bin/bash
# Build .skill files from source skill directories
# Usage: ./scripts/build-skills.sh [skill-name]
# If no skill specified, builds all skills

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
DIST_DIR="$REPO_ROOT/dist"

# Create dist directory if it doesn't exist
mkdir -p "$DIST_DIR"

# If a specific skill is provided, build only that one
if [ $# -gt 0 ]; then
  SKILLS_TO_BUILD="$1"
else
  # Build all skills
  SKILLS_TO_BUILD=$(ls -d "$SKILLS_DIR"/*/ | xargs -n 1 basename)
fi

for skill in $SKILLS_TO_BUILD; do
  SKILL_DIR="$SKILLS_DIR/$skill"

  if [ ! -d "$SKILL_DIR" ]; then
    echo "❌ Skill not found: $skill"
    exit 1
  fi

  if [ ! -f "$SKILL_DIR/SKILL.md" ]; then
    echo "❌ Missing SKILL.md in $skill"
    exit 1
  fi

  echo "📦 Building $skill.skill..."

  # Remove stale dist file so zip creates fresh (not appends)
  rm -f "$DIST_DIR/$skill.skill"

  # Create ZIP archive containing SKILL.md and all subdirectories (assets, references, etc)
  cd "$SKILL_DIR"
  zip -q -r "$DIST_DIR/$skill.skill" SKILL.md */ 2>/dev/null || zip -q -r "$DIST_DIR/$skill.skill" SKILL.md
  cd "$REPO_ROOT"

  echo "✅ Created dist/$skill.skill"
done

echo ""
echo "✨ All skills built successfully!"
