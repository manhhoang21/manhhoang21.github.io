source "https://rubygems.org"

# Cùng bộ gem với GitHub Pages (Jekyll 3.x, Ruby Sass 3.7.x) để build ở CI ra đúng như site thật.
# Xem phiên bản đang dùng: https://pages.github.com/versions/
gem "github-pages", group: :jekyll_plugins

# Kiểm tra link nội bộ bị chết trong CI (.github/workflows/kiem-tra.yml)
group :test do
  gem "html-proofer", "~> 5.0"
end

# Ruby 3+ không còn kèm webrick, cần cho `jekyll serve`
gem "webrick"

# Windows không có sẵn dữ liệu múi giờ
platforms :windows, :jruby do
  gem "tzinfo-data"
end
