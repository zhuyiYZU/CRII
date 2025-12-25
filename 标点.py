import pandas as pd


def replace_punctuation_in_column(csv_file, column_name, output_file=None):
    """
    替换CSV文件中指定列的英文标点为中文标点

    参数:
        csv_file: 输入CSV文件路径
        column_name: 要处理的列名
        output_file: 输出文件路径(可选，默认覆盖原文件)
    """
    # 读取CSV文件
    df = pd.read_csv(csv_file)

    # 定义替换规则
    replacements = {
        ',': '，',  # 英文逗号 → 中文逗号
        ';': '；'  # 英文分号 → 中文分号
    }

    # 对指定列进行替换
    df[column_name] = df[column_name].astype(str).replace(replacements, regex=True)

    # 保存结果
    if output_file:
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
    else:
        df.to_csv(csv_file, index=False, encoding='utf-8-sig')

    print(f"替换完成！结果已保存至: {output_file if output_file else csv_file}")


# 使用示例
replace_punctuation_in_column(
    csv_file='input.csv',  # 输入文件
    column_name='content',  # 要处理的列名
    output_file='output.csv'  # 输出文件(可选)
)