
// 对表格包装
// `table` to `div.table-wrapper > table`
document.querySelectorAll('table').forEach(table => {
  const wrapper = document.createElement('div');
  wrapper.classList.add('table-wrapper');

  table.parentNode.insertBefore(wrapper, table);
  wrapper.appendChild(table);
});

// 简单的支持种子的随机数生成器
// 目前主要用于视觉设计
function SimpleRandom(seed=555) {
  return () => {
    const x = Math.sin(seed++) * 10000;
    return x - Math.floor(x);
  };
}

const random_iter = SimpleRandom();


