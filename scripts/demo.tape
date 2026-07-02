# VHS tape for the README demo GIF (https://github.com/charmbracelet/vhs)
#
# Run from the repo root with contractor-bid installed on PATH:
#   brew install vhs   # or: go install github.com/charmbracelet/vhs@latest
#   vhs scripts/demo.tape
#
# Produces docs/assets/demo.gif (README) and docs/assets/demo.webm
# (landing page hero). Uses only the fictional fences-gates demo data.

Output docs/assets/demo.gif
Output docs/assets/demo.webm

Set FontSize 16
Set Width 1200
Set Height 640
Set Theme "Catppuccin Mocha"
Set TypingSpeed 40ms
Set Shell "bash"

Hide
Type `rm -rf /tmp/cb-demo && mkdir -p /tmp/cb-demo/bids && cp -R examples/fictional-fences-gates-demo /tmp/cb-demo/bids/070126-fictional-cedar-park-fence && export BID=/tmp/cb-demo/bids/070126-fictional-cedar-park-fence && clear`
Enter
Show

Type "# A 340-page bid package just landed. Watch."
Enter
Sleep 1.5s

Type "contractor-bid triage $BID --profile fences-gates"
Enter
Sleep 4s

Type "contractor-bid build-packets $BID"
Enter
Sleep 3s

Type "contractor-bid build-workbook $BID --profile fences-gates"
Enter
Sleep 3s

Type "contractor-bid check $BID --profile fences-gates --today 2026-06-30"
Enter
Sleep 3.5s

Type "contractor-bid package-sendoff $BID"
Enter
Sleep 3s

Type "ls $BID/bid-package-working/"
Enter
Sleep 4s
