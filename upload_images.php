<?php
// 上传图片
define('UPLOAD_KEY', 'dfas&*32k24_42#asdf');
$name = $_POST['name'];

$md5 = $_POST['md5'];


if ($md5 != md5(md5($name).UPLOAD_KEY)) {
	echo 'error md5';exit;
}

if (!preg_match('#images/\d+\-\d+\-\d+/#', $name)) {
	echo 'error name';exit;
}

if(isImage($_FILES["file"]["tmp_name"]) === false){
    echo 'error image';exit;
}

$new_file = newFile($name);

move_uploaded_file($_FILES["file"]["tmp_name"], $new_file);


function isImage($filename){
    $types = '.gif|.jpeg|.jpg|.png|.bmp';//定义检查的图片类型
    if(file_exists($filename)){
        $info = getimagesize($filename);
        $ext = image_type_to_extension($info['2']);
        return stripos($types,$ext);
    }else{
        return false;
    }
}

function newFile($name) {
	if (!$name) {
		echo 'error name';exit;
	}
	$dir = dirname(__FILE__).'/bbsimages';
	$basename = basename($name);
	preg_match('#images/(.+?)/#', $name, $m);	
	if (!$m['1']) {
		echo 'error date';exit;
	}
	if (!is_dir($dir)) {
		@mkdir($dir, 0777, true);
	}
	if (!is_dir($dir.'/'.$m['1'])) {
		@mkdir($dir.'/'.$m['1'], 0777, true);
	}
	return $dir.'/'.$m['1'].'/'.$basename ;

}