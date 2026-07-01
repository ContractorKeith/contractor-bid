# Homebrew Packaging

`contractor-bid.rb` is a tap-ready formula template for the v0.2.1 release.

Before publishing it to a Homebrew tap:

1. Cut and push the `v0.2.1` tag.
2. Compute the GitHub source tarball SHA:

   ```bash
   curl -L https://github.com/ContractorKeith/contractor-bid/archive/refs/tags/v0.2.1.tar.gz \
     | shasum -a 256
   ```

3. Replace `REPLACE_WITH_V0_2_0_TARBALL_SHA256`.
4. Replace the MCP 1.8.1 resource SHA with the exact source tarball SHA for that version.
5. Run:

   ```bash
   brew install --build-from-source ./contractor-bid.rb
   brew test contractor-bid
   ```

The formula depends on `poppler` so Homebrew users do not need to install PDF tools manually.
