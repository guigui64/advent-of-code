local id = vim.api.nvim_create_augroup("AOC2022", { clear = true })

vim.api.nvim_create_autocmd("BufNewFile", {
  group = id,
  pattern = "*.ts",
  command = "0read skeleton.ts",
})
