# Makefile for compiling all LaTeX reports
# 一键编译所有实验报告的 LaTeX 文件

# LaTeX 编译器设置
LATEX = xelatex
LATEX_FLAGS = -interaction=nonstopmode -halt-on-error -file-line-error

# 查找所有 .tex 文件
TEX_FILES := $(shell find . -name "*.tex" -not -path "*/\.*" | sort)

# 生成对应的 PDF 文件列表
PDF_FILES := $(TEX_FILES:.tex=.pdf)

# 默认目标：编译所有 PDF
all: $(PDF_FILES)
	@echo "=========================================="
	@echo "所有实验报告编译完成！"
	@echo "=========================================="

# 编译单个 PDF 文件的规则
%.pdf: %.tex
	@echo "正在编译: $<"
	@TEX_DIR=$$(dirname "$<"); \
	TEX_BASE=$$(basename "$<" .tex); \
	cd "$$TEX_DIR" && \
	$(LATEX) $(LATEX_FLAGS) "$$TEX_BASE" > /dev/null 2>&1 || \
	$(LATEX) $(LATEX_FLAGS) "$$TEX_BASE" && \
	$(LATEX) $(LATEX_FLAGS) "$$TEX_BASE" > /dev/null 2>&1 || true
	@if [ -f "$@" ]; then \
		echo "✓ 成功: $@"; \
	else \
		echo "✗ 失败: $@"; \
	fi

# 清理所有编译中间文件
clean:
	@echo "正在清理编译中间文件..."
	@find . -type f \( \
		-name "*.aux" -o \
		-name "*.log" -o \
		-name "*.out" -o \
		-name "*.synctex.gz" -o \
		-name "*.fdb_latexmk" -o \
		-name "*.fls" -o \
		-name "*.xdv" \
	\) -not -path "*/\.*" -delete
	@echo "清理完成！"

# 清理所有 PDF 文件
clean-pdf:
	@echo "正在清理所有 PDF 文件..."
	@find . -name "*.pdf" -not -path "*/\.*" -not -name "大学物理实验*.pdf" -delete
	@echo "PDF 文件清理完成！"

# 完全清理（包括 PDF）
distclean: clean clean-pdf
	@echo "完全清理完成！"

# 列出所有需要编译的文件
list:
	@echo "找到以下 .tex 文件："
	@find . -name "*.tex" -not -path "*/\.*" | sort | while read file; do \
		echo "  - $$file"; \
	done
	@echo ""
	@echo "共 $$(find . -name "*.tex" -not -path "*/\.*" | wc -l | tr -d ' ') 个文件"

# 编译单个实验报告（用法: make compile TEX=path/to/file.tex）
compile:
ifndef TEX
	@echo "错误: 请指定要编译的文件"
	@echo "用法: make compile TEX=path/to/file.tex"
	@exit 1
endif
	@if [ ! -f "$(TEX)" ]; then \
		echo "错误: 文件 $(TEX) 不存在"; \
		exit 1; \
	fi
	@echo "正在编译: $(TEX)"
	@TEX_DIR=$$(dirname "$(TEX)"); \
	TEX_BASE=$$(basename "$(TEX)" .tex); \
	cd "$$TEX_DIR" && \
	$(LATEX) $(LATEX_FLAGS) "$$TEX_BASE" && \
	$(LATEX) $(LATEX_FLAGS) "$$TEX_BASE"

# 并行编译（使用 make -j）
.PHONY: all clean clean-pdf distclean list compile

# 帮助信息
help:
	@echo "Makefile 使用说明："
	@echo ""
	@echo "   make          - 编译所有 .tex 文件生成 PDF"
	@echo "   make clean    - 清理所有编译中间文件（.aux, .log 等）"
	@echo "   make clean-pdf - 清理所有生成的 PDF 文件"
	@echo "   make distclean - 完全清理（包括 PDF 和中间文件）"
	@echo "   make list     - 列出所有需要编译的 .tex 文件"
	@echo "   make compile TEX=path/to/file.tex - 编译单个文件"
	@echo "   make help     - 显示此帮助信息"
	@echo ""
	@echo "提示：使用 'make -j4' 可以并行编译，加快速度"