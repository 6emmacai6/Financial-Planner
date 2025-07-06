#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 20:08:29 2025

@author: apple
"""

import streamlit as st

st.title("Financial Planning Tool")
st.write("CRR's app！")

# 输入金额
amount = st.number_input("请输入投资金额（元）", min_value=0.0, step=100.0)

# 输入年化收益率
rate = st.slider("年化收益率（%）", min_value=0.0, max_value=20.0, value=5.0)

# 输入投资年数
years = st.number_input("投资年数", min_value=1, max_value=50, value=5)

# 计算复利
final = amount * ((1 + rate / 100) ** years)
st.write(f"预计{years}年后本息合计：{final:.2f} 元")
 
