# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
from lxml import etree
import re
from urllib import quote

print quote('http://www.mengsang.com/duorou/list_1_1.html')
print quote('http://www.mengsang.com/duorou/jingtianke/nishilianshu/Echeveria-Ben Badis.html')

html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>多肉草球-仙人球属怎么养护种植？- 多肉植物1000多种品种图鉴 - 梦桑阁</title>
<meta name="keywords" content="草球" />
<meta name="description" content="草球 仙人掌科(Cactaceae) / 仙人球属(Echinopsis) 别名:长盛球 简介 长盛球，植物年龄长达80年。幼期茎呈球形，10年以上慢慢呈椭圆形，夏季为花期开花3朵以上（去除厕生小球，10年以上年龄可有一年三次花期花期花朵数量可达10枝以上），花期需转移至阴凉处" />
<script language="javascript" type="text/javascript" src="http://www.mengsang.com/include/dedeajax2.js"></script>
<link rel="stylesheet" type="text/css" href="http://www.mengsang.com/templets/ms/ms2013/css/global.css" />
<link rel="stylesheet" type="text/css" href="http://www.mengsang.com/templets/ms/ms2013/css/no-theme/jquery-ui-1.10.3.custom.css"/>
<script type="text/javascript" src="http://www.mengsang.com/templets/ms/ms2013/scripts/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="http://www.mengsang.com/templets/ms/ms2013/scripts/main.js"></script>
<script type="text/javascript" src="http://www.mengsang.com/templets/ms/ms2013/scripts/jquery-ui-1.10.3.min.js"></script>
<style>
.xiaotu {
	max-width: 100px;
	max-height: 100px;
	height:auto;
 zoom:expression( function(e) {
if(e.width>e.height) {
if (e.width>100) {
e.height = e.height*(100 /e.width);
e.width=100;
}
}
else {
if (e.height>100) {
e.width = e.width*(100 /e.height);
e.height=100;
}
}
e.style.zoom = '1';
}
(this));
 overflow:hidden;
}
</style>
</head>
<body class="articleview">
<div class="topBar">
  <div class="topBarCon pageWrapper">
    <table width="1024px" align="center">
      <tr>
        <td width="85"><a href="http://www.mengsang.com/"><img src="http://www.mengsang.com/templets/ms/ms2013/images/logoms.png" width="151" height="71" alt="梦桑阁" /></a>
          <div class="topBarLeft layout"><a href="http://www.mengsang.com/"   class="selected">首页</a><a href="http://www.mengsang.com/duorou/"  >多肉植物</a><a href="http://www.mengsang.com/zhiwu-ask">多肉养护</a><a href="http://www.mengsang.com/zhiwu-photo/">多肉壁纸</a><a href="https://shop118034908.taobao.com/" target="_blank" >淘宝直销</a><a href="http://www.mengsang.com/atms" target="_blank" >联系我们</a><a href="#" target="_blank" >全国大棚</a></div></td>
        <td align="right"><div class="topBarRight" id="statusBar">
          <div class="toplinks"><span>[ <a href="javascript:window.external.AddFavorite('http://www.mengsang.com','梦桑阁')">加入收藏</a> ]</span><a name="gotop"></a></div></div></td>
      </tr>
    </table>
  </div>
  <!--topBarCon-->
</div>
<!--topBar-->

<div class="headerWrapper">
	<div class="header pageWrapper">
    	<table width="100%">
        	<tr>
            	<td width="420"><a href="index.htm"  class="logo"><img src="http://www.mengsang.com/templets/ms/ms2013/images/new/logoIndex.png" /></a></td>
                <td></td>
                <td class="pt20" align="right">
                	<div class="headerRight">

					<form action="http://www.mengsang.com/plus/search.php" onsubmit="return dosearch();">

                        <span class="searchBox vm mr10 fRight"><span class="searchTxtBox fLeft mr5"><input value="" id="top_search_text" name="keyword" inputdefault="请输入你喜欢植物名字"  type="text" class="searchTxt" /></span><input type="submit" value="" class="searchBtn fLeft"/></span>
					</form>
                    </div>
                </td>
            </tr>
        </table>
    </div>
</div><!--headerWrapper-->
<!-- /header -->
<div class="pageWrapper mainWrapper">
  <div class="layout contentBox">
  <div class="mainBoxTitle"><span class="mainBoxTitleCon"><a href='http://www.mengsang.com/'>主页</a> > <a href='http://www.mengsang.com/category/'>全部植物</a> > <a href='http://www.mengsang.com/duorou/'>多肉植物</a> > <a href='http://www.mengsang.com/duorou/xianrenzhangke/'>仙人掌科（Cactaceae）</a> > <a href='http://www.mengsang.com/duorou/xianrenzhangke/xianrenqiushu/'>仙人球属</a> >  </span></div>
    <div class="cbLeft">
      <div class="mainBox">
        <div class="mainBoxCon">
          <div class="imgCenter"><span><ul>

	<li>
		<img alt="草球" src="/uploads/allimg/170405/1-1F4051951155P.jpg" style="border: 0px; vertical-align: middle; width: 512px; height: 512px;" /></li>	<li>
		<h2>
			草球</h2>
	</li>
	<li>
		<table border="0" cellpadding="0" cellspacing="0" width="100%">
			<tbody>
				<tr>
					<td>
						<a href='http://www.mengsang.com/duorou/xianrenzhangke/' target='_blank'><u>仙人掌科</u></a>(Cactaceae) / 仙人球属(Echinopsis)</td>
				</tr>
				<tr>
					<td>
						别名:长盛球</td>
				</tr>
			</tbody>
		</table>
	</li>
	<li>
		<h3>
			简介</h3>
		长盛球，植物年龄长达80年。幼期茎呈球形，10年以上慢慢呈椭圆形，夏季为花期开花3朵以上（去除厕生小球，10年以上年龄可有一年三次花期花期花朵数量可达10枝以上），花期需转移至阴凉处能增加花期时间一般有7-10天。花着生于纵棱刺丛中，银白色或粉红色，长喇叭形，长可达20厘米。球体常侧生出许多小球，形态优美、雅致。 长盛球耐旱.怕水湿.冬季较其他仙人球而言较耐寒冷,可耐2~5度的低温.喜欢生于排水良好的沙质土壤。</li>
	<li>
		生长季：夏种<br />
		日照量：一般<br />
		浇水量：较少</li>
</ul>
</span> </div>
          <div class="imgCenter"><span style="color:#C30">如您可纠错，补充请发Email 至 <a class="__cf_email__" href="/cdn-cgi/l/email-protection" data-cfemail="9df7f4e8fee8f2ddf0f8f3faeefcf3fab3fef2f0">[email&#160;protected]</a><script data-cfhash='f9e31' type="text/javascript">/* <![CDATA[ */!function(t,e,r,n,c,a,p){try{t=document.currentScript||function(){for(t=document.getElementsByTagName('script'),e=t.length;e--;)if(t[e].getAttribute('data-cfhash'))return t[e]}();if(t&&(c=t.previousSibling)){p=t.parentNode;if(a=c.getAttribute('data-cfemail')){for(e='',r='0x'+a.substr(0,2)|0,n=2;a.length-n;n+=2)e+='%'+('0'+('0x'+a.substr(n,2)^r).toString(16)).slice(-2);p.replaceChild(document.createTextNode(decodeURIComponent(e)),c)}p.removeChild(t)}}catch(u){}}()/* ]]> */</script>，请大家来帮助萌友们一起成长和学习！</span><a target="_blank" href="http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=hbSyvbSztLS0s8X09Kvm6ug" style="text-decoration:none;"><img src="http://rescdn.qqmail.com/zh_CN/htmledition/images/function/qm_open/ico_mailme_02.png"/></a> </div>
          <div class="imgCenter"><img src="http://www.mengsang.com/images/2weima.jpg"  alt="多肉二唯码"/></div>
                <div class="layout pl10 pr10 mt10"><span class="fLeft vm"><a href="#" class="tBtn1 mr10">上一篇：<a href='http://www.mengsang.com/duorou/xianrenzhangke/xianrenqiushu/20174883.html'>白檀 Peanut Cactus</a> </a>　　　　</span>　<span class="fLeft vm"><a href="#" class="tBtn1 mr10">下一篇：没有了 </a></span></div>
      <div class="layout pl10 pr10"> <span class="fRight vm">
        <!-- Baidu Button BEGIN -->
        <div id="bdshare" class="bdshare_t bds_tools get-codes-bdshare"> <a class="bds_qzone"></a> <a class="bds_tsina"></a> <a class="bds_tqq"></a> <a class="bds_renren"></a> <a class="bds_t163"></a> <span class="bds_more"></span> </div>
        <!-- Baidu Button END --></span></div>

        </div>
        <div class="borderTop pt10 pl10 pr10 pb20"> <b>图片关键字</b>
          <div class="imgTags">草球</div>
        </div>
      </div>

    </div>
    <div class="cbRight">
      <div class="mainBox">
        <div class="mainBoxTitle"><span class="mainBoxTitleCon">草球</span></div>
        <div class="mainBoxCon pl20 pr20 pt10 pb10">
          <table class="tTable" width="100%">
            <tr>
              <th width="50">项目</th>
              <th width="100">数据</th>
              <th width="70">项目</th>
              <th width="70">数据</th>
            </tr>
            <tr>
              <td><span class="circle"><b>繁殖</b></span></td>
              <td>扦插,分株</td>
              <td><span class="circle"><b>易活度</b></span></td>
              <td><img src="http://www.mengsang.com/templets/ms/ms2013/images/x3.png"/></td>
            </tr>
            <tr>
              <td><span class="circle"><b>季节</b></span></td>
              <td>春秋种型</td>
              <td><span class="circle"><b>温　度</b></span></td>
              <td>　10-25  ℃</td>
            </tr>
            <tr class="last">
              <td><span class="circle"><b>日照</b></span></td>
              <td><img src="http://www.mengsang.com/templets/ms/ms2013/images/3.png"/></td>
              <td><span class="circle"><b>浇水量</b></span></b></span></td>
              <td><img src="http://www.mengsang.com/templets/ms/ms2013/images/s3.png"/></td>
            </tr>
          </table>
          <div class="borderTop  pt10 pl10 pr10 pb20">
            <div>
              <div class="pt5"><span class="c999"><strong>日照说明：</strong>一个太阳代表每天日照1小时，2个代表2小时</span></div>
              <div class="pt5"><span class="c999"><strong>浇水说明：</strong>一个水滴代表一个月浇水1次，2个代表一个月2次，浇水时间并不严格，因季节与气候、地域、有所不同，尽供参考！</span></div>
              <div class="pt5"></div>
              <div class="pt5"><span class="c999">大类 / 属：</span>仙人球属</div>
              <div class="pt5"><span class="c999">中文种名：</span></div>
              <div class="pt5"><span class="c999">英文学名：</span></div>
            </div>
          </div>
        </div>
      </div>
      <div class="mainBox mt30">
        <div class="mainBoxTitle"><span class="mainBoxTitleCon">从梦桑阁淘宝店购买多肉（暗号：梦桑）</span></div>
        <div class="mainBoxCon pl20 pr20 pt10 pb10">
<a target="_blank" href="https://shop118034908.taobao.com/" style="text-decoration:none;"><img src="http://www.mengsang.com/tb/anhao.jpg"/></a>
        </div>
      </div>
      <div class="mainBox mt30">
        <div class="mainBoxTitle"><a href="http://www.mengsang.com/zhiwu-ask/" class="mainBoxTitleMore" target="_blank">更多 >></a><span class="mainBoxTitleCon">精品文章</span></div>
        <div class="mainBoxCon pb10">
            <div>
                        <ul>
           <li class="c999 bbline ml20"><span class="indexgrt pl20"><a href='http://www.mengsang.com/zhiwu-ask/huahuizhensuo/4938.html'>多肉要怎么对待土壤板结</a></span><span class="pr10">　　　</span>2017/05/27 </li>
<li class="c999 bbline ml20"><span class="indexgrt pl20"><a href='http://www.mengsang.com/zhiwu-ask/huahuizhensuo/4937.html'>多肉植物砍头你知道多少</a></span><span class="pr10">　　　</span>2017/05/27 </li>
<li class="c999 bbline ml20"><span class="indexgrt pl20"><a href='http://www.mengsang.com/zhiwu-ask/huahuizhensuo/4936.html'>多肉植物度夏如同渡劫</a></span><span class="pr10">　　　</span>2017/05/27 </li>
<li class="c999 bbline ml20"><span class="indexgrt pl20"><a href='http://www.mengsang.com/zhiwu-ask/huahuizhensuo/4935.html'>如果盆土永远都是潮土，那多肉植物还能被养胖吗？</a></span><span class="pr10">　　　</span>2017/05/27 </li>
<li class="c999 bbline ml20"><span class="indexgrt pl20"><a href='http://www.mengsang.com/zhiwu-ask/huahuizhensuo/4934.html'>敲警钟：千万别用气雾剂给肉肉杀虫</a></span><span class="pr10">　　　</span>2017/05/27 </li>

           <li class="c999 bbline ml20"><span class="indexgrt pl20"><a href="http://www.mengsang.com/zhiwu-ask/huahuizhensuo/4431.html">到底多肉可以漫步雨天吗？</a>
           </span><span class="pr10">　　　</span>2014/04/08</li>
           <li class="c999 bbline ml20"><span class="indexgrt pl20"> <a href="http://www.mengsang.com/zhiwu-ask/huahuizhensuo/4502.html">多肉植物-发现与治理虫害！</a>
           </span><span class="pr10">　　　</span>2014/04/08</li>
           <li class="c999 bbline ml20"><span class="indexgrt pl20">
           <a href="http://www.mengsang.com/zhiwu-ask/huahuizhensuo/4448.html">网购植物后的栽种上盆缓苗方式</a> </span><span class="pr10">　　　</span>2014/04/08</li>

           <li class="c999 bbline ml20"><span class="indexgrt pl20"><a href="http://www.mengsang.com/zhiwu-ask/huahuizhensuo/4463.html">踏着多肉尸体来教您度夏经验</a>
           </span><span class="pr10">　　　</span>2014/04/08</li>
           <li class="c999 bbline ml20"><span class="indexgrt pl20"> <a href="http://www.mengsang.com/zhiwu-ask/duorouzhiwu/4458.html">多肉植物16种可用土</a>
           </span><span class="pr10">　　　</span>2014/04/08</li>
           <li class="c999 bbline ml20"><span class="indexgrt pl20">
                      <a href="http://www.mengsang.com/zhiwu-ask/duorouzhiwu/4453.html">关于高锰酸钾的那些事</a></span><span class="pr10">　　　</span>2014/04/08</li>
           <li class="c999 bbline ml20"><span class="indexgrt pl20">
           <a href="http://www.mengsang.com/zhiwu-ask/duorouzhiwu/4494.html">自制环保酵素让你的多肉植物理漂亮</a>
           </span><span class="pr10">　　　</span>2014/04/08</li>
           <li class="c999 bbline ml20"><span class="indexgrt pl20"><a href="http://www.mengsang.com/zhiwu-ask/bozhongjiyumiao/4449.html">多肉植物繁殖的魅力 之 叶插</a>
           </span><span class="pr10">　　　</span>2014/04/08</li>
              </ul>
                    </div>
        </div>
      </div>
      <div class="mainBox mt30">
        <div class="mainBoxTitle"><a href="#" class="mainBoxTitleMore" target="_blank">更多 >></a><span class="mainBoxTitleCon">相似植物</span></div>
        <div class="mainBoxCon pb10">
          <ul class="layout sameUl">
            <li>
              <table>
                <tr>
                  <td valign="bottom"><a href="http://www.mengsang.com/duorou/xianrenzhangke/xianrenqiushu/20174932.html"class='preview' title="草球" target="_blank"><img src="http://www.mengsang.com/uploads/allimg/170405/1-1F4051951155P-lp.jpg" alt="草球" width="100" height="100"/></a></td>
                </tr>
              </table>
            </li>
<li>
              <table>
                <tr>
                  <td valign="bottom"><a href="http://www.mengsang.com/duorou/xianrenzhangke/xianrenqiushu/20174883.html"class='preview' title="白檀 Peanut Cactus" target="_blank"><img src="http://www.mengsang.com/uploads/allimg/170309/1-1F309204R1139-lp.jpg" alt="白檀 Peanut Cactus" width="100" height="100"/></a></td>
                </tr>
              </table>
            </li>
<li>
              <table>
                <tr>
                  <td valign="bottom"><a href="http://www.mengsang.com/duorou/xianrenzhangke/xianrenqiushu/Echinopsis-cinnabarina.html"class='preview' title="龟甲丸 Echinopsis cinnabarina" target="_blank"><img src="http://www.mengsang.com/uploads/allimg/131018/11344643A-0-lp.jpg" alt="龟甲丸 Echinopsis cinnabarina" width="100" height="100"/></a></td>
                </tr>
              </table>
            </li>

          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="footerWrapper">
  <div class="footerSearch">
    <table>
      <form action="http://www.mengsang.com/plus/search.php">
        <tr>
          <td width="460"><input value="" name="keyword" type="text" class="footerSearchTxt" inputdefault="请输入你喜欢植物名字"  /></td>
          <td width="83"><input value="" type="submit" value="" class="footerSearchBtn"/></td>
        </tr>
      </form>
    </table>
  </div>
  <div class="footerCon pageWrapper">
    <table width="100%">
      <tr>
        <td class="footerTop"  valign="top"><div class="layout footerTopDl">
        <ul>
        <h3>慎重声明：<a name="gobottom"></a></h3>
        <li>1、本站所有资源来源于网络收集！免费分享于网络！</li>
        <li>2、所有信息尽供大家参考，一切后果，本站一律不负责。</li>
        <li>3、如本站有内容伤害了您的利益，请通过mowei#vip.qq.com告之，在看到邮件的同时马上处理。</li>
        <li>4、本站为多肉植物、水族等个人爱好所建，如您有合作意向请通过以上邮箱告诉我！</li>
        </ul>
          </div></td>
        <td align="right" valign="top"><div class="footerTopRight">
            <p><span><a href="http://www.mengsang.com/plus/heightsearch.php" target="_blank">高级搜索</a></span><br/>
              <a href="http://www.mengsang.com/data/sitemap.html" target="_blank">网站地图</a></p>
            <p><span><a href="http://www.mengsang.com/tags.php">TAG标签</a></span><br/>
              <a href="http://www.mengsang.com/data/rssmap.html" class="rss">RSS订阅 </a></p>
            <p><span><a href="http://www.mengsang.com/pifa">多肉批发</a></span><br/>
              <a href="http://www.mengsang.com/data/aboutms">多肉大棚</a></p>
          </div></td>
      </tr>
      <tr class="footerDown">
        <td><p class="powered">
		Powered by <a href="#" title="梦桑阁，养花卉心得！--家庭花卉首选利器。" target="_blank"><strong>Mengsang</strong></a> &#169; 2004-2011 <a href="#" target="_blank">mengsang.com</a> Inc.<br /><div class="copyright">Copyright &copy; 2002-2011 MengSang 梦桑阁 <a href=http://www.dedecms.com target='_blank'>Power by DedeCms</a>&#160;&#160;沪ICP备12019302号-3 <a href="http://www.zx110.org/"><img src="http://www.mengsang.com/templets/ms/ms2013/images/zxlogo.jpg" width="100" height="25" alt="征集网" /></a></div></p> <script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_5776432'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s13.cnzz.com/stat.php%3Fid%3D5776432%26show%3Dpic1' type='text/javascript'%3E%3C/script%3E"));</script>
<!-- /powered --></td>
        <td align="right"><img src="http://www.mengsang.com/templets/ms/ms2013/images/footerlogo.jpg" alt="梦桑阁" /></td>
      </tr>
    </table>
  </div>
</div>
<!--footerWrapper-->
<!-- //底部模板 -->
<div class="footer w960 center mt1 clear">
    <div class="footer_left"></div>
    <div class="footer_body">

   </div>
   <div class="footer_right"></div>
</div>


<div class="weixin">
    <img src="http://www.mengsang.com/templets/ms/ms2013/images/wx-icon.png" width="40" height="112" />
    <div class="xixi">
        <img src="http://www.mengsang.com/templets/ms/ms2013/images/weixin.jpg" width="150" height="150" />
    </div>
</div>

<!-- /footer -->
<script type="text/javascript" id="bdshare_js" data="type=tools&uid=637414" ></script>
<script type="text/javascript" id="bdshell_js"></script>
<script type="text/javascript">
document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + Math.ceil(new Date()/3600000)
</script>
</body>
</html>
"""

page = pq(html)

for each in page('.cbLeft li').items():

    if u'http://www.mengsang.com' in each.html():

        for td in each('table td').items():

            item = td.text()
            if u'科' in item:
                print item
                pattern = re.compile(u'(.*?) \((.*?)\) / (.*?)\((.*?)\)')
                match = re.search(pattern, item)
                if match:
                    family_name = match.group(1)
                    print family_name
                    family_terminology = match.group(2)
                    print family_terminology
                    genus_name = match.group(3)
                    print genus_name
                    genus_terminology = match.group(4)
                    print genus_terminology

            if u'别名' in item:
                alias = item[3:]
                print alias

            if u'原产地:' in item:
                area = item[4:]
                print area

    if u'简介' in each.html():
        description = each.text()[2:].strip()
        print description

    li = '<li>' + each.html() + '</li>'
    if u'生长季' in li:
        pattern = re.compile(u'生长季：(.*?)<')
        match = re.search(pattern, li)
        if match:
            growth_season = match.group(1)
            print growth_season

    if u'日照量' in li:
        pattern = re.compile(u'日照量：(.*?)<')
        match = re.search(pattern, li)
        if match:
            sunshine = match.group(1)
            print sunshine

    if u'浇水量' in li:
        pattern = re.compile(u'浇水量：(.*?)<')
        match = re.search(pattern, li)
        if match:
            moisture = match.group(1)
            print moisture

items = list(page('.cbRight .tTable td:odd').items())
breed_pattern = items[0].text()
print breed_pattern
breed_difficulty = items[1]('img').attr.src[-5:-4]
print breed_difficulty
temperature = items[3].text()
print temperature
sunshine = items[4]('img').attr.src[-5:-4]
print sunshine
moisture = items[5]('img').attr.src[-5:-4]
print moisture

div = page('.cbRight .borderTop div').html()
pattern = re.compile(u'<span.*?>英文学名：</span>(.*?)</div>')
match = re.search(pattern, div)
if match:
    terminology = match.group(1)
    print terminology
