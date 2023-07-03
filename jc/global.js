// 获取所有表格元素
const tables = document.querySelectorAll('table');

// 遍历每个表格
tables.forEach(table => {
  // 创建一个新的 div 元素作为包装容器
  const wrapper = document.createElement('div');
  wrapper.classList.add('table-wrapper');

  // 将当前表格放入包装容器中
  table.parentNode.insertBefore(wrapper, table);

  // 移动当前表格到包装容器中
  wrapper.appendChild(table);
});
