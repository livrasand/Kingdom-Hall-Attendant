<svelte:head>
  <title>Oradores públicos</title>
</svelte:head>

<div class="tabnav">
   <nav class="tabnav-tabs" aria-label="Foo bar">
      <a class="tabnav-tab" href="/dashboard/oradorespublicos" aria-current="page">Locales</a>
      <a class="tabnav-tab" href="/dashboard/oradorespublicos/foraneos">Foraneos</a>
   </nav>
</div>

<div class="container-lg clearfix">
  <div class="col-4 float-left">
     <div class="Box">
        <div class="Box-row d-flex flex-items-center">
           <div class="flex-auto">
              <strong>Apellidos, Nombre</strong>
           </div>
           <button class="btn mr-2 btn-sm" type="button">
              <!-- <%= octicon "search" %> -->
              <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
                 <path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path>
              </svg>
           </button>
        </div>
     </div>
  </div>
  <div class="col-8 float-left p-4 mt-n4">
     <form>
        <input class="form-control" type="text" placeholder="Nombres" aria-label="Nombres" style="width: 49%;" />
        <input class="form-control" type="text" placeholder="Apellidos" aria-label="Apellidos" style="width:49%;" />
        <div class="form-checkbox mt-2">
           <label>
           <input type="checkbox" />
           <em class="highlight">Aprobado para salir</em>
           </label>
        </div>
        <input class="form-control width-full mt-2" type="email" placeholder="Correo electrónico" aria-label="Correo electrónico" />
        <input class="form-control width-full mt-2" type="number" placeholder="Celular" aria-label="Celular" />
        <input class="form-control width-full mt-2" type="number" placeholder="Teléfono" aria-label="Teléfono" />
        <div class="radio-group mt-2">
           <input class="radio-input" id="option-anciano" type="radio" name="nombramientos">
           <label class="radio-label" for="option-anciano">Anciano</label>
           <input class="radio-input" id="option-siervom" type="radio" name="nombramientos">
           <label class="radio-label" for="option-siervom">Siervo ministerial</label>   
        </div>
        <p class="f5 mb-n3 mt-3">Bosquejos preparados</p>
        <div class="container-lg clearfix mt-3">
           <div class="col-2 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">1</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">7</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">13</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">19</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">25</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">31</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">37</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">43</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">49</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">55</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">61</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">67</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">73</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">79</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">85</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">91</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">103</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">109</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">115</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">121</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">127</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">133</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">139</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">145</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">151</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">157</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">163</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">169</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">175</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">181</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">187</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">193</em>
                 </label>
              </div>
           </div>
           <div class="col-2 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">2</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">8</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">14</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">20</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">26</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">32</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">38</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">44</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">50</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">56</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">62</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">68</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">74</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">80</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">86</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">92</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">104</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">110</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">116</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">122</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">128</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">134</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">140</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">146</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">152</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">158</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">164</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">170</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">176</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">182</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">188</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">194</em>
                 </label>
              </div>
           </div>
           <div class="col-2 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">3</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">9</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">15</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">21</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">27</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">33</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">39</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">45</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">51</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">57</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">63</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">69</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">75</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">81</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">87</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">93</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">105</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">111</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">117</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">123</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">129</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">135</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">141</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">147</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">153</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">159</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">165</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">171</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">177</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">183</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">189</em>
                 </label>
              </div>
           </div>
           <div class="col-2 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">4</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">10</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">16</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">22</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">28</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">34</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">40</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">46</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">52</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">58</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">64</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">70</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">76</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">82</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">88</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">94</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">106</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">112</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">118</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">124</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">130</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">136</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">142</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">148</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">154</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">160</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">166</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">172</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">178</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">184</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">190</em>
                 </label>
              </div>
           </div>
           <div class="col-2 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">5</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">11</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">17</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">23</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">29</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">35</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">41</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">47</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">53</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">59</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">65</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">71</em>                           
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">77</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">83</em>                           
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">89</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">95</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">107</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">113</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">119</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">125</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">131</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">137</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">143</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">149</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">155</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">161</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">167</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">173</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">179</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">185</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">191</em>
                 </label>
              </div>
           </div>
           <div class="col-2 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">6</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">12</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">18</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">24</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">30</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">36</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">42</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">48</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">54</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">60</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">66</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">72</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">78</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">84</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">90</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">96</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">108</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">114</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">120</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">126</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">132</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">138</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">144</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">150</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">156</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">162</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">168</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">174</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">180</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">186</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">192</em>
                 </label>
              </div>
           </div>
        </div>
        <br><br>
        <div class="form-actions">
           <button type="submit" class="btn btn-primary">Guardar</button>
           <button type="button" class="btn btn-danger">
              <!-- <%= octicon "trashcan" %> -->
              <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
                 <path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path>
              </svg>
              <span>Eliminar</span>
           </button>
           <button type="button" class="btn btn-outline">
              <span data-component="text">
                 <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" style="display: inline-block; vertical-align: text-bottom;">
                    <path  d="M.989 8 .064 2.68a1.342 1.342 0 0 1 1.85-1.462l13.402 5.744a1.13 1.13 0 0 1 0 2.076L1.913 14.782a1.343 1.343 0 0 1-1.85-1.463L.99 8Zm.603-5.288L2.38 7.25h4.87a.75.75 0 0 1 0 1.5H2.38l-.788 4.538L13.929 8Z"></path>
                 </svg>
                 <span contenteditable="true" class="Text-sc-125xb1i-0 cTqQd ml-2">Enviar datos a una congregación</span>
              </span>
           </button>
        </div>
     </form>
  </div>
</div>
