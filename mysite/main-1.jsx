/**
 * v0 by Vercel.
 * @see https://v0.dev/t/sPnhGg14mBz
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import Link from "next/link";
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar";

export default function Component() {
  return (
    <div className="flex flex-col min-h-[100dvh]">
      <header className="px-4 lg:px-6 h-14 flex items-center">
        <Link
          href="#"
          className="flex items-center justify-center"
          prefetch={false}
        >
          <MountainIcon className="h-6 w-6" />
          <span className="sr-only">Acme Software Agency</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Link
            href="#"
            className="text-sm font-medium hover:underline underline-offset-4"
            prefetch={false}
          >
            Services
          </Link>
          <Link
            href="#"
            className="text-sm font-medium hover:underline underline-offset-4"
            prefetch={false}
          >
            Work
          </Link>
          <Link
            href="#"
            className="text-sm font-medium hover:underline underline-offset-4"
            prefetch={false}
          >
            About
          </Link>
          <Link
            href="#"
            className="text-sm font-medium hover:underline underline-offset-4"
            prefetch={false}
          >
            Contact
          </Link>
        </nav>
      </header>
      <main className="flex-1">
        <section className="w-full py-12 sm:py-24 md:py-32 lg:py-40 xl:py-48">
          <div className="container px-4 md:px-6">
            <div className="grid gap-6 lg:grid-cols-[1fr_400px] lg:gap-12 xl:grid-cols-[1fr_600px]">
              <div className="flex flex-col justify-center space-y-4">
                <div className="space-y-2">
                  <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none">
                    Elevate Your Digital Presence
                  </h1>
                  <p className="max-w-[600px] text-muted-foreground md:text-xl">
                    Acme Software Agency crafts exceptional digital experiences
                    that drive results for our clients.
                  </p>
                </div>
                <div className="flex flex-col gap-2 min-[400px]:flex-row">
                  <Link
                    href="#"
                    className="inline-flex h-10 items-center justify-center rounded-md bg-primary px-8 text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50"
                    prefetch={false}
                  >
                    Get a Quote
                  </Link>
                  <Link
                    href="#"
                    className="inline-flex h-10 items-center justify-center rounded-md border border-input bg-background px-8 text-sm font-medium shadow-sm transition-colors hover:bg-accent hover:text-accent-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50"
                    prefetch={false}
                  >
                    Learn More
                  </Link>
                </div>
              </div>
              <img
                src="/placeholder.svg"
                width="550"
                height="550"
                alt="Hero"
                className="mx-auto aspect-video overflow-hidden rounded-xl object-cover sm:w-full lg:order-last lg:aspect-square"
              />
            </div>
          </div>
        </section>
        <section className="w-full py-12 sm:py-24 md:py-32 lg:py-40 xl:py-48 bg-muted">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">
                  Our Services
                </h2>
                <p className="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Acme Software Agency offers a comprehensive suite of digital
                  services to help your business thrive.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl items-start gap-8 sm:grid-cols-2 md:grid-cols-3 md:gap-12 lg:gap-16">
              <div className="grid gap-4">
                <div className="flex items-center gap-4">
                  <div className="rounded-full bg-primary p-3 text-primary-foreground">
                    <CodeIcon className="h-6 w-6" />
                  </div>
                  <h3 className="text-lg font-bold">Web Development</h3>
                </div>
                <p className="text-muted-foreground">
                  Our expert developers create custom, responsive websites and
                  web applications tailored to your business needs.
                </p>
              </div>
              <div className="grid gap-4">
                <div className="flex items-center gap-4">
                  <div className="rounded-full bg-primary p-3 text-primary-foreground">
                    <SmartphoneIcon className="h-6 w-6" />
                  </div>
                  <h3 className="text-lg font-bold">Mobile Development</h3>
                </div>
                <p className="text-muted-foreground">
                  We design and develop cutting-edge mobile apps for iOS and
                  Android, ensuring a seamless user experience.
                </p>
              </div>
              <div className="grid gap-4">
                <div className="flex items-center gap-4">
                  <div className="rounded-full bg-primary p-3 text-primary-foreground">
                    <BrushIcon className="h-6 w-6" />
                  </div>
                  <h3 className="text-lg font-bold">UI/UX Design</h3>
                </div>
                <p className="text-muted-foreground">
                  Our talented designers create visually stunning and
                  user-friendly interfaces that captivate your audience.
                </p>
              </div>
              <div className="grid gap-4">
                <div className="flex items-center gap-4">
                  <div className="rounded-full bg-primary p-3 text-primary-foreground">
                    <RocketIcon className="h-6 w-6" />
                  </div>
                  <h3 className="text-lg font-bold">Digital Marketing</h3>
                </div>
                <p className="text-muted-foreground">
                  We leverage the latest digital marketing strategies to
                  increase your online visibility and drive conversions.
                </p>
              </div>
              <div className="grid gap-4">
                <div className="flex items-center gap-4">
                  <div className="rounded-full bg-primary p-3 text-primary-foreground">
                    <DatabaseIcon className="h-6 w-6" />
                  </div>
                  <h3 className="text-lg font-bold">Data Analytics</h3>
                </div>
                <p className="text-muted-foreground">
                  Our data experts provide in-depth analysis and insights to
                  help you make informed business decisions.
                </p>
              </div>
              <div className="grid gap-4">
                <div className="flex items-center gap-4">
                  <div className="rounded-full bg-primary p-3 text-primary-foreground">
                    <CloudIcon className="h-6 w-6" />
                  </div>
                  <h3 className="text-lg font-bold">Cloud Solutions</h3>
                </div>
                <p className="text-muted-foreground">
                  We offer scalable and secure cloud-based solutions to
                  streamline your operations and boost productivity.
                </p>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 sm:py-24 md:py-32 lg:py-40 xl:py-48">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">
                  Our Work
                </h2>
                <p className="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Check out some of our recent projects and see how we've helped
                  our clients achieve their goals.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl items-start gap-8 sm:grid-cols-2 md:grid-cols-3 md:gap-12 lg:gap-16">
              <div className="grid gap-4">
                <img
                  src="/placeholder.svg"
                  width="550"
                  height="310"
                  alt="Project 1"
                  className="mx-auto aspect-video overflow-hidden rounded-xl object-cover"
                />
                <div>
                  <h3 className="text-lg font-bold">Project 1</h3>
                  <p className="text-muted-foreground">
                    A modern e-commerce website for a leading fashion brand.
                  </p>
                </div>
              </div>
              <div className="grid gap-4">
                <img
                  src="/placeholder.svg"
                  width="550"
                  height="310"
                  alt="Project 2"
                  className="mx-auto aspect-video overflow-hidden rounded-xl object-cover"
                />
                <div>
                  <h3 className="text-lg font-bold">Project 2</h3>
                  <p className="text-muted-foreground">
                    A custom web application for a SaaS startup.
                  </p>
                </div>
              </div>
              <div className="grid gap-4">
                <img
                  src="/placeholder.svg"
                  width="550"
                  height="310"
                  alt="Project 3"
                  className="mx-auto aspect-video overflow-hidden rounded-xl object-cover"
                />
                <div>
                  <h3 className="text-lg font-bold">Project 3</h3>
                  <p className="text-muted-foreground">
                    A responsive mobile app for a fitness company.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 sm:py-24 md:py-32 lg:py-40 xl:py-48 bg-muted">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">
                  What Our Clients Say
                </h2>
                <p className="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Hear from our satisfied clients about their experience working
                  with Acme Software Agency.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl items-start gap-8 sm:grid-cols-2 md:grid-cols-3 md:gap-12 lg:gap-16">
              <div className="grid gap-4">
                <blockquote className="rounded-lg border bg-background p-6 shadow">
                  <div className="flex items-center gap-4">
                    <Avatar>
                      <AvatarImage src="/placeholder-user.jpg" />
                      <AvatarFallback>JD</AvatarFallback>
                    </Avatar>
                    <div>
                      <p className="text-sm font-medium leading-none">
                        John Doe
                      </p>
                      <p className="text-sm text-muted-foreground">
                        CEO, Acme Corp
                      </p>
                    </div>
                  </div>
                  <p className="mt-4 text-muted-foreground">
                    "Acme Software Agency has been an invaluable partner in\n
                    helping us transform our online presence. Their team's\n
                    expertise and dedication have been instrumental in\n driving
                    our business forward."
                  </p>
                </blockquote>
              </div>
              <div className="grid gap-4">
                <blockquote className="rounded-lg border bg-background p-6 shadow">
                  <div className="flex items-center gap-4">
                    <Avatar>
                      <AvatarImage src="/placeholder-user.jpg" />
                      <AvatarFallback>SM</AvatarFallback>
                    </Avatar>
                    <div>
                      <p className="text-sm font-medium leading-none">
                        Sarah Miller
                      </p>
                      <p className="text-sm text-muted-foreground">
                        CMO, Startup X
                      </p>
                    </div>
                  </div>
                  <p className="mt-4 text-muted-foreground">
                    "Working with Acme Software Agency has been a game-changer\n
                    for our startup. Their team's innovative approach and\n
                    attention to detail have helped us create a truly\n
                    remarkable digital experience for our customers."
                  </p>
                </blockquote>
              </div>
              <div className="grid gap-4">
                <blockquote className="rounded-lg border bg-background p-6 shadow">
                  <div className="flex items-center gap-4">
                    <Avatar>
                      <AvatarImage src="/placeholder-user.jpg" />
                      <AvatarFallback>LW</AvatarFallback>
                    </Avatar>
                    <div>
                      <p className="text-sm font-medium leading-none">
                        Lisa Wang
                      </p>
                      <p className="text-sm text-muted-foreground">
                        CTO, Acme Tech
                      </p>
                    </div>
                  </div>
                  <p className="mt-4 text-muted-foreground">
                    "Acme Software Agency's technical expertise and\n
                    forward-thinking approach have been invaluable in helping\n
                    us modernize our technology stack and stay ahead of the\n
                    curve."
                  </p>
                </blockquote>
              </div>
            </div>
          </div>
        </section>
      </main>
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t">
        <p className="text-xs text-muted-foreground">
          &copy; 2024 Acme Software Agency. All rights reserved.
        </p>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link
            href="#"
            className="text-xs hover:underline underline-offset-4"
            prefetch={false}
          >
            Terms of Service
          </Link>
          <Link
            href="#"
            className="text-xs hover:underline underline-offset-4"
            prefetch={false}
          >
            Privacy
          </Link>
        </nav>
      </footer>
    </div>
  );
}

function BrushIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m9.06 11.9 8.07-8.06a2.85 2.85 0 1 1 4.03 4.03l-8.06 8.08" />
      <path d="M7.07 14.94c-1.66 0-3 1.35-3 3.02 0 1.33-2.5 1.52-2 2.02 1.08 1.1 2.49 2.02 4 2.02 2.2 0 4-1.8 4-4.04a3.01 3.01 0 0 0-3-3.02z" />
    </svg>
  );
}

function CloudIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z" />
    </svg>
  );
}

function CodeIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <polyline points="16 18 22 12 16 6" />
      <polyline points="8 6 2 12 8 18" />
    </svg>
  );
}

function DatabaseIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <ellipse cx="12" cy="5" rx="9" ry="3" />
      <path d="M3 5V19A9 3 0 0 0 21 19V5" />
      <path d="M3 12A9 3 0 0 0 21 12" />
    </svg>
  );
}

function MountainIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m8 3 4 8 5-5 5 15H2L8 3z" />
    </svg>
  );
}

function RocketIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z" />
      <path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z" />
      <path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0" />
      <path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5" />
    </svg>
  );
}

function SmartphoneIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <rect width="14" height="20" x="5" y="2" rx="2" ry="2" />
      <path d="M12 18h.01" />
    </svg>
  );
}

function XIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M18 6 6 18" />
      <path d="m6 6 12 12" />
    </svg>
  );
}
