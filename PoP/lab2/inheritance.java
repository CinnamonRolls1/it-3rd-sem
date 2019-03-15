class cube{
	double length,width,height;
	cube(double l,double w, double h){
		length=l;
		width=w;
		height=h;
	}
	double volume(){
		return length*height*width;
	}
}
class cubemass extends cube{
	double mass;
	cubemass(double l,double w,double h,double m){
		super(l,w,h);
		mass=m;
	}
}
class inheritance{
	public static void main(String[] args) {
		cubemass cube=new cubemass(2,2,2,40);
		System.out.println("Volume & mass: "+cube.volume()+" "+cube.mass);
	}
}