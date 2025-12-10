// Vercel Node.js中转函数（适配QQ开放平台）
export default async function handler(req, res) {
  // 1. 处理GET请求：返回echostr，通过QQ校验
  if (req.method === 'GET') {
    const echostr = req.query.echostr || '';
    res.status(200).send(echostr);
    return;
  }

  // 2. 处理POST请求：转发到你的广州云函数
  if (req.method === 'POST') {
    try {
      // 替换为你的云函数URL
      const cloudFuncUrl = 'https://1391451970-73tz9amjql.ap-guangzhou.tencentscf.com';
      // 转发请求到云函数
      const response = await fetch(cloudFuncUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(req.body)
      });
      // 返回云函数的响应
      const data = await response.json();
      res.status(200).json(data);
    } catch (error) {
      res.status(500).json({ error: '转发失败：' + error.message });
    }
    return;
  }

  // 3. 不支持的请求方法
  res.status(405).send('Method Not Allowed');
}
