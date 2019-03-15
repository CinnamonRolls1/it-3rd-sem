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
class cubestrength extends cubemass{
	double strength;
	cubestrength(double l,double w,double h,double m,double s){
		super(l,w,h,m);
		strength=s;
	}
}
class mult{
	public static void main(String[] args) {
		cubestrength cube=new cubestrength(3,3,3,15,4);
		System.out.println("cube volume, mass and strength are "+cube.volume()+", "+cube.mass+" and "+cube.strength);
	}
}