const axios = require('axios');

module.exports = async (req, res) => {
  const { year, week } = req.query;
  const url = `https://wol.jw.org/es/wol/meetings/r4/lp-s/${year}/${week}`;

  try {
    const response = await axios.get(url);
    res.status(200).send(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch data' });
  }
};
