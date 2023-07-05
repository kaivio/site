// 获取所有文章标题元素
const articleTitles = document.querySelectorAll('h2, h3, h3');

// 创建目录容器元素
const tocContainer = document.createElement('div');
tocContainer.classList.add('toc-container');

// 创建目录列表元素
const tocList = document.createElement('ul');
tocList.classList.add('toc-list');

// 遍历每个文章标题元素，并创建对应的目录项和跳转链接
articleTitles.forEach((title) => {
  const listItem = document.createElement('li');
  listItem.classList.add('toc-level-'+title.tagName.charAt(1))
  const link = document.createElement('a');

  link.textContent = title.textContent;

  link.textContent = title.textContent;
  link.setAttribute('href','#'+title.textContent)

  const anchor = document.createElement('a');
  anchor.setAttribute('id', title.textContent)
  anchor.classList.add('anchor')

  title.parentNode.insertBefore(anchor, title.nextSibling);



   // 将链接添加到列表项中，并将列表项添加到目录列表中
   listItem.appendChild(link);
   tocList.appendChild(listItem);


});

// 将目录列表插入到目录容器中
tocContainer.appendChild(tocList);

// 找到第一个文章标题的父节点，并在其后插入整个目录容器
const h1 = document.querySelector('h1');
h1.parentNode.insertBefore(tocContainer,h1.nextSibling);
