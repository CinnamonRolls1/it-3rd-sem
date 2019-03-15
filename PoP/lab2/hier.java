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
class cubeid extends cube{
	int id;
	cubeid(double l,double w,double h,int i){
		super(l,w,h);
		id=i;
	}
}
class hier{
	public static void main(String[] args) {
		cubeid cube=new cubeid(4,4,4,10356);
		System.out.println("cube volume and id are "+cube.volume()+" and "+cube.id);
		cubemass cube2=new cubemass(4,4,4,50);
		System.out.println("Cube mass is "+cube2.mass);
	}
}