module "ec2" {
  source        = "./ec2"
  key_name      = var.key_name
  instance_type = var.instance_type
}