class ContractorBid < Formula
  include Language::Python::Virtualenv

  # Template for the v0.2.0 tap update. Before publishing, replace the source SHA
  # and regenerate the Python resource blocks with `brew update-python-resources`.
  desc "AI-ready commercial construction bid workspaces for subcontractors"
  homepage "https://github.com/ContractorKeith/contractor-bid"
  url "https://github.com/ContractorKeith/contractor-bid/archive/refs/tags/v0.2.0.tar.gz"
  sha256 "REPLACE_WITH_V0_2_0_TARBALL_SHA256"
  license "MIT"
  head "https://github.com/ContractorKeith/contractor-bid.git", branch: "main"

  depends_on "python@3.12"
  depends_on "poppler"

  resource "openpyxl" do
    url "https://files.pythonhosted.org/packages/source/o/openpyxl/openpyxl-3.1.5.tar.gz"
    sha256 "5282c12b107bffeef825f4617dc029afaf41d0ea60823bbb665ef3079dc79de2"
  end

  resource "pypdf" do
    url "https://files.pythonhosted.org/packages/source/p/pypdf/pypdf-4.3.1.tar.gz"
    sha256 "f3c6c085aa38b5729c96c03be9d44e4c4dc5e3fef175c07c4feb9e0d48f1a25d"
  end

  resource "mcp" do
    url "https://files.pythonhosted.org/packages/source/m/mcp/mcp-1.8.1.tar.gz"
    sha256 "REPLACE_WITH_MCP_1_8_1_TARBALL_SHA256"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/contractor-bid --version")
    assert_match "contractor-bid environment check", shell_output("#{bin}/contractor-bid doctor")
    assert_path_exists bin/"contractor-bid-mcp"
  end
end
